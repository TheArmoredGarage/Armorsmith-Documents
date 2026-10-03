"""Generate an openly documented v1 storage fixture using only the standard library.

MIT licensed; see ../../LICENSE. The legacy-shaped bytes test storage and
reconstruction, not rendering or the complete legacy scene grammar.
"""

import argparse
import base64
import hashlib
import json
from pathlib import Path
import zipfile


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=4) + "\n").encode("utf-8")


def generate(output):
    output = output.resolve()
    names = ("Example", "Example.costume", "Example Published.costume", "Example.armor")
    if any((output / name).exists() for name in names):
        raise FileExistsError("Choose an output directory without existing Example files.")
    output.mkdir(parents=True, exist_ok=True)
    root = output / "Example"
    dependencies = {}

    def put(directory, stem, extension, data):
        digest = hashlib.sha256(data).hexdigest()
        relative = f"{directory}/{stem}-{digest}.{extension}"
        dependencies[relative] = data
        return relative

    def role(directory, name, data):
        return {
            "path": put(directory, name, "bin", data),
            "sha256": hashlib.sha256(data).hexdigest(),
            "size": len(data),
        }

    def record(directory, stem, value):
        return {"path": put(directory, stem, "json", json_bytes(value))}

    header = b'VERS 23\r\nDESC "Storage example"\r\nAUTH "Example author"\r\n'
    footer = b'AVTR\r\n{\r\nJSON {"avatar": true}\r\n}\r\n'
    model = (
        b'MESH 1\r\n{\r\nMSNM "Helmet"\r\nMSID abc\r\n'
        b'VSIZ 3\r\nDATA illustrative-geometry\r\n}\r\n'
    )
    owner_prefix = b'WKSP 6\r\n{\r\nWKNM "Owner"\r\nGUID 101\r\nMARG 10 10 10 10}\r\n'
    owner_suffix = b'JSON {"patterns": [1, 2]}\r\n}\r\n'
    shared_workspace = (
        b'WKSP 6\r\n{\r\nWKNM "Shared"\r\nGUID 102\r\nMARG 10 10 10 10}\r\n'
        b'MESH 1\r\n{\r\nWKNM "Owner"\r\nMSNM "Helmet"\r\nMSID abc\r\n}\r\n'
        b'JSON {}\r\n}\r\n'
    )
    model_id = "model-101-abc"
    state_directory = "state/costume-state"
    model_directory = f"models/{model_id}"
    model_record = {
        "id": model_id,
        "kind": "model",
        "name": "Helmet",
        "codec": "armor-chunks",
        "files": {
            "source": role(model_directory, "source", model),
            "preview": role(model_directory, "preview", model.replace(b"illustrative-geometry", b"illustrative-preview")),
            "original": role(model_directory, "original", b"o Helmet\nv 0 0 0\nv 1 0 0\nv 0 1 0\nf 1 2 3\n"),
        },
        "originalSource": {"storage": "bundled", "name": "helmet.obj", "role": "original"},
        "previewCodec": "armor-chunks",
        "previewTargetTriangles": 100000,
        "previewTriangleCount": 1,
        "sourceTriangleCount": 1,
        "sourceVertexCount": 3,
        "previewSourceSha256": hashlib.sha256(model).hexdigest(),
        "exampleProduct": {"note": "Preserve unfamiliar fields when editing other data."},
    }
    state_record = {
        "id": "costume-state",
        "kind": "state",
        "codec": "armor-chunks",
        "files": {
            "header": role(state_directory, "header", header),
            "footer": role(state_directory, "footer", footer),
        },
    }
    b64 = lambda data: base64.b64encode(data).decode("ascii")
    owner = {
        "id": "workspace-101",
        "name": "Owner",
        "codec": "armor-chunks",
        "assets": [model_id],
        "legacyLayout": [b64(owner_prefix), {"asset": model_id}, b64(owner_suffix)],
    }
    shared = {
        "id": "workspace-102",
        "name": "Shared",
        "codec": "armor-chunks",
        "assets": [model_id],
        "legacyLayout": [b64(shared_workspace)],
    }
    manifest = {
        "format": "costume",
        "version": 1,
        "id": "f47b3d60-e566-4b17-9316-2b83c1a83f88",
        "name": "Example",
        "assets": {
            model_id: record(model_directory, "model", model_record),
            "costume-state": record(state_directory, "state", state_record),
        },
        "workspaces": {
            owner["id"]: record("workspaces/workspace-101", "workspace", owner),
            shared["id"]: record("workspaces/workspace-102", "workspace", shared),
        },
        "workspaceOrder": [owner["id"], shared["id"]],
    }
    for relative, data in dependencies.items():
        destination = root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
    manifest_data = json_bytes(manifest)
    (output / "Example.costume").write_bytes(manifest_data)
    with zipfile.ZipFile(output / "Example Published.costume", "w", zipfile.ZIP_DEFLATED) as bundle:
        # Fixed metadata makes the example package reproducible. No directory entries.
        for name, data in [("manifest.json", manifest_data), *sorted(dependencies.items())]:
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, data)
    (output / "Example.armor").write_bytes(header + owner_prefix + model + owner_suffix + shared_workspace + footer)
    print(f"Generated editable, bundled, and reconstruction fixtures in {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="Directory without existing Example files")
    generate(parser.parse_args().output)
