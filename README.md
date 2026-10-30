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

Keep corrections for the current public version separate from upcoming interface changes. The 2.1.1.0 documentation covers Workbench and the foam workflow, illustrated with creator-supplied application captures. Version notes distinguish these instructions from 2.1.0.10; documentation publication does not establish installer availability.

The immediate Printable Figure correction removes a nonworking, disabled feature from supported export instructions. It does not enable that implementation.

Application Perforce changelists and the read-only source mirror supply implementation evidence. Release status also needs an identified application build. See [the 2.1.1.0 review checklist](drafts/2.1.1.0-review.md) for source references, capture IDs, and pending native checks. Review files under `drafts/` are excluded by `.mintignore`.

## Foam documentation visibility

Seven foam workflow pages are visible under the Foam patterns navigation tab after the creator's capture review and publication authorization. The surface-details availability page remains hidden/noindex because decorative hardware behavior was not verified. Hidden navigation is not access control.

See [the capture review](drafts/2.1.1.0-capture-review.md) and asset manifest for accepted images, corrections, and verification limits. Environment Settings is an internal dev-build tool and is excluded from customer procedures. Printable Figure remains disabled.

## Publishing

The configured Mintlify GitHub integration deploys the default branch. Merge current-release corrections through the normal review flow. Keep upcoming-release changes in draft until their release checks are complete. After an authorized merge, verify the affected live text and images rather than assuming deployment succeeded.
