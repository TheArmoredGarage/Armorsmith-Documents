# Documentation project instructions

## Product and source

This repository contains the Armorsmith Designer help site. Pages are MDX with YAML frontmatter; navigation, theme, and branding live in `docs.json`.

Application development uses Perforce as the primary source and a read-only GitHub mirror. This documentation repository uses Git branches and pull requests. An application feature being present in source does not establish that it is released.

Use the configured Mintlify MCP tools when available. Otherwise edit this repository directly and validate with the Mintlify CLI.

## Writing

- Write for costume and cosplay makers. Explain when to use a feature, prerequisites, practical steps, and the expected result.
- Use active voice, second person, concise sentences, and sentence-case headings.
- Use exact visible UI labels in bold. Use code formatting for filenames, commands, and source references.
- Keep implementation details and source-validation notes out of user instructions. Put release review notes under `drafts/`, which is ignored by Mintlify.
- Preserve existing URLs when changing a title or reorganizing a page. Check inbound fragments when replacing headings.

## Terminology

- A **workspace** contains model and pattern content.
- **Workshop** is the model-and-pattern work view; **Costume** is the avatar-fitting view.
- **Workbench** is the dock with **Browse**, **Edit**, and **Inspect** pages.
- **Transforms** is the separate numeric position, rotation, and scale panel. Do not call it Property Grid.
- **Drawing layers** organize drafting content. **Foam layers** position raised pieces at a physical height above a base.
- **Preview Color** is the foam appearance control; it does not select physical stock or establish material-library availability.

## Release boundaries

Keep current-release fixes separate from upcoming-release instructions. Label upcoming version-specific pages and hold their branch until the candidate's controls and behavior are verified. Do not present source-only observations as native application tests.

The foam navigation tab and its eight pages remain hidden; pages also retain `noindex: true` until the complete workflow is checked for release. Hidden pages remain publicly reachable by URL. Do not add broken image placeholders while captures are pending.

Printable Figure is disabled because it does not work. Do not document miniature STL export as supported or expose its dormant implementation. Printable Details, model-derived Create Patterns, and foam build sheets require explicit release qualification before documenting their entry points as available.

## Validation and publication

Before a PR is ready to merge, run:

```text
python -m unittest discover -s tests -p 'test_*.py' -v
npx --yes mint@4.2.988 validate
npx --yes mint@4.2.988 broken-links --check-anchors
```

Inspect the rendered pages and verify changed procedures against an identified application build. Use real matching-version captures, readable UI scale, descriptive captions and useful alt text. Reuse an accurate image instead of recapturing it solely for visual polish.

Pushing to the configured default branch can deploy to the public site. Prepare changes on branches/PRs and check the served result after an authorized release.
