# Armorsmith Designer help

This repository is the Mintlify source for [Armorsmith Designer help](https://armorsmith-designer.mintlify.site/introduction). Read [AGENTS.md](AGENTS.md) for writing conventions and product terminology.

## Edit and preview

Use a branch for documentation work. Pages are `.mdx`; `docs.json` controls navigation. Preserve existing routes and check related tutorial steps when changing a reference page.

Run `npx --yes mint@4.2.988 dev` from the repository root to preview locally. For checks, run:

```text
python -m unittest discover -s tests -p 'test_*.py' -v
npx --yes mint@4.2.988 validate
npx --yes mint@4.2.988 broken-links --check-anchors
```

The existing GitHub Actions workflow runs licensing checks and Mintlify validation for its configured changed paths.

## Current and upcoming releases

Keep corrections for the current public version separate from upcoming interface changes. The 2.1.1.0 documentation branch describes the upcoming Workbench and foam workflow; its per-page version notes do not establish that a public build has shipped.

The immediate Printable Figure correction removes a nonworking, disabled feature from supported export instructions. It does not enable that implementation.

Application Perforce changelists and the read-only source mirror supply implementation evidence. Release status also needs an identified application build. See [the 2.1.1.0 review checklist](drafts/2.1.1.0-review.md) for source references, capture IDs, and pending native checks. Review files under `drafts/` are excluded by `.mintignore`.

## Foam documentation visibility

The eight foam guides already exist on `main` under `foam-preview/` and are served by direct URL. Their tab has `hidden: true`; the pages also have `hidden: true` and `noindex: true`. Hidden navigation is not access control.

Keep those fields while the workflow is unreleased or unverified. Before making the section visible, run the layered-bracer tutorial in the release candidate, verify every exposed entry point and output, complete essential matching-version captures, and validate navigation and links. Do not add withheld features just because their code exists.

## Publishing

The configured Mintlify GitHub integration deploys the default branch. Merge current-release corrections through the normal review flow. Keep upcoming-release changes in draft until their release checks are complete. After an authorized merge, verify the affected live text and images rather than assuming deployment succeeded.
