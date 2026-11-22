# Paint Materials documentation — review before publication

Date prepared: November 20, 2026
Target: Armorsmith Designer 2.1.2.0 painting release (build awaiting owner confirmation)
Status: DRAFT — all four user-supplied screenshots are uploaded to this PR branch and linked in the appropriate MDX pages. Release/build verification and documentation checks remain outstanding. Do not merge before approval.

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

- [ ] Identify the exact application build/version shown in the supplied screenshots; Paint Materials is visibly enabled in Workshop.
- [ ] Verify Browse → Material Passes transitions in the target build; the supplied close-up confirms its stack and toolbar labels.
- [ ] Prepare a new imported model and confirm first-pass naming and save/reopen.
- [ ] Fill → Model result is visible in supplied screenshot; test Fill → Surface including preview and threshold behavior.
- [ ] Test Fill → Drag Box and its Hit Testing settings.
- [ ] Confirm active-pass erasing, EyeDropper/ESC and brush shortcuts.
- [ ] Confirm pass reorder, opacity, visibility, and undo/redo.
- [ ] Confirm labels for visibility, Wrap Into Crevices, and Finish.
- [ ] Confirm when Weathering Pass and Decal Pass can be selected; exclude unfinished or experimental controls from release text.

## Screenshot captures uploaded to the PR branch

All four user-supplied captures were uploaded by the owner to `images/` on this branch, and the resulting file sizes match the supplied originals. The reference and tutorial pages now include image links and descriptive alt text. These are repository-image checks, not rendered Mintlify checks.

| Upload this PNG to the branch | Use in | Suggested accessible image caption |
| --- | --- | --- |
| `images/paint-brush-2120.png` | Paint tool introduction and Brush section | "Workshop showing a helmet with Paint Materials active, Brush selected, and paint color and flow controls visible." |
| `images/paint-fill-2120.png` | Fill reference and tutorial step 3 | "Helmet filled blue with Fill mode set to Model; selection, opacity, and material controls are visible." |
| `images/paint-weathering-2120.png` | Weathering Pass overview | "A blue helmet with Black Wash weathering applied around its edges and recesses; effect strength and bleed controls are open." |
| `images/paint-passes-2120.png` | Browse → Material Passes section and Workbench overview | "Browse showing two Weathering Passes above Paint 1, with pass controls for adding, moving, visibility, and opacity." |

Image syntax and captions are present in `painting/paint-materials.mdx` and `painting/paint-tutorial.mdx`. The fourth capture is a close-up of Browse rather than a full-window view, which is suitable for the control reference.

Optional next-week improvements: a dedicated brush stroke before/after, full-page Browse capture, and an advanced Edge Wear/Black Wash tutorial. Retain these captures as baseline documentation; additional captures are editorial improvements rather than blockers once the build is verified.

## Publishing gates

Run the documented unit/Mintlify checks, inspect rendered pages, resolve link/anchor warnings, and verify procedures in the identified application build before moving the PR from draft or merging. Repository file existence and Markdown link targets were checked; local Mintlify CLI and native app tests have not been run.
