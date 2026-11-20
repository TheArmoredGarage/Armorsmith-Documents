# Paint Materials documentation — review before publication

Date prepared: November 20, 2026
Target: Armorsmith Designer 2.1.1.0 documentation
Status: DRAFT — owner verification and screenshots required; do not merge solely on source inspection.

## Scope

- New Paint Materials reference and beginner tutorial.
- Added Material Passes to the existing Workbench/Workshop descriptions.
- Added visible navigation entries on this review branch, not on main.
- Paint Islands is a separate feature and keeps its existing guide.

## Source-based verification

Read-only source inspection was used for UI wording and behavior. Representative files:
- `Code/FE/PaintingEditors.h` — Paint Materials entry, Brush/Erase/Eyedropper/Fill mode selection, material preparation.
- `Code/FE/PaintEditorPanel.h` — mode labels, brush and material controls, fill options, visibility.
- `Code/FE/MaterialPassPanel.cpp` — Browse pass stack, addition/duplication/reordering/opacity.
- `Code/Tests/MaterialPassM5Review.txt` — native review still pending for some material-pass interactions in the recorded handoff.

The Paint Materials UI code is conditional on testing/build flags in inspected source. Do NOT interpret source presence or documentation as confirmation of public-release availability.

## Creator review in identified build

- [ ] Identify the application build/version and confirm Paint Materials is enabled in its Workshop toolbar.
- [ ] Check Browse → Material Passes, tab visibility, and Edit tool transitions.
- [ ] Prepare a new imported model and confirm first-pass naming and save/reopen.
- [ ] Test Fill → Model and Fill → Surface (including preview/threshold behavior).
- [ ] Test Fill → Drag Box and its Hit Testing settings.
- [ ] Confirm active-pass erasing, EyeDropper/ESC and brush shortcuts.
- [ ] Confirm pass reorder, opacity, visibility, and undo/redo.
- [ ] Confirm labels for visibility, Wrap Into Crevices, and Finish.
- [ ] Confirm when Weathering Pass and Decal Pass can be selected; exclude unfinished or experimental controls from release text.

## Screenshots requested

Add real images from the same approved build, preferably 1600px+ wide with readable UI:
1. Workshop with imported model, toolbar Paint Materials button, Workbench Edit open. Suggested: `images/paint-entry-2110.png`.
2. Browse → Material Passes showing Base/Accent passes, visibility and opacity. Suggested: `images/paint-passes-2110.png`.
3. Edit with Fill selected, Surface / Model modes and threshold visible. Suggested: `images/paint-fill-2110.png`.
4. Same model before/after or completed base-plus-accent result. Suggested: `images/paint-finished-2110.png`.

Once supplied and verified, add image references, alt text, captions, and crosslinks at the relevant instructions. Do not add nonexistent image links.

## Publishing gates

Run the documented unit/Mintlify checks, inspect rendered pages, resolve link/anchor warnings, and verify procedures in the identified application build before moving the PR from draft or merging. No checks were run during source-only drafting.
