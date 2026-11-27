# Shape creation and corner tools — release review

Prepared: November 27, 2026
Status: DRAFT / review required. Source inspected read-only; do not merge solely because the controls exist in the current working tree.

## Scope

- Added `patterns/shape-creation-and-corners.mdx` for rectangle, circle and line creation, exact dimensions, live Fillet/Chamfer, and troubleshooting.
- Updated `patterns/pattern-layout.mdx`, `foam-preview/drawing-and-editing.mdx`, and the layered bracer tutorial with route-preserving links and updated gestures.
- Added the new page to Templates & Patterns navigation in `docs.json`.
- Existing 2.1.1.0 pages retain their previous version labels and explicitly qualify the new workflow as appearing in newer builds.

## Source evidence

Connected Armorsmith Source is read-only at `C:\Dev`. The connection does **not** expose Perforce CLI, changelists, submitted revisions, or a diff against a known prior changeset. This documents current local source behavior; do not characterize it as a Perforce history audit.

Relevant source at the time of review:
- `Armorsmith_QT/Armorsmith_QT/Code/SplineTools.cpp` — `SplineCornerHandle` (drag, live preview, right-click exact dialog, direct numeric entry, Escape, undo); rectangle/circle creation and dialogs; line anchors; repeated primitive creation. Modified UTC 2026-11-27T19:21:14.936406.
- `Armorsmith_QT/Armorsmith_QT/Code/SplineTools.h` — public creation and geometry tool contracts.
- `Armorsmith_QT/Armorsmith_QT/Code/FE/SplinePrecisionTools.h` — selected vertices, same outline constraint, uniformly scaled transform requirement, Fillet Corner… and Chamfer Corner… actions.
- `Armorsmith_QT/Armorsmith_QT/Code/FE/PatternToolbar.h` — Vertex Tools placement inside Edit Shape and precision-actions routing.
- `Armorsmith_QT/Armorsmith_QT/Code/FE/PatternCreateMenu.h` — Create menu lists Line, Rectangle, Circle, Text, Image.
- `Armorsmith_QT/Armorsmith_QT/Code/FE/CreateCircle.cpp` — exact radius, diameter, circumference and optional repeat settings.

Do not rely on the legacy `EditSplineWidget.cpp` spinbox controls as the current user flow: the updated editing surface exposes gesture-first corner tools.

## Native release verification

- [ ] Identify the specific installed build / release version and ensure the shape tool update is actually enabled for customers.
- [ ] Verify Create → Rectangle drag, Shift-square, click/right-click exact dimension dialog, Cancel, and repeated rectangle creation.
- [ ] Verify Create → Circle drag from center and exact Radius / Diameter / Circumference options and repeated circles.
- [ ] Verify Create → Line anchors, Ctrl curve handles, Return for open line, click-start close, Backspace, right-click exact segment and Escape.
- [ ] Verify Edit Shape → Vertex selection on one outline, Ctrl multi-select and that Fillet Corner… / Chamfer Corner… appear under Vertex Tools.
- [ ] Verify drag preview, right-click exact value dialog, direct numeric entry + Enter, Escape cancel, and undo.
- [ ] Confirm Fillet uses **Radius (mm)** and Chamfer uses **Distance along each curve (mm)** and that large values are rejected atomically.
- [ ] Verify a non-uniformly scaled outline produces the expected restriction, while a uniformly scaled outline succeeds.
- [ ] Confirm changes to 2D outline vs 3D foam Edge Finish are described correctly in an installed build.
- [ ] Capture the new Create dimensions dialog and a selected two-corner Fillet/Chamfer viewport if screenshots would materially help. Existing edit-shape screenshots may predate these controls.
- [ ] Run `python -m unittest discover -s tests -p 'test_*.py' -v`.
- [ ] Run `npx --yes mint@4.2.988 validate`.
- [ ] Run `npx --yes mint@4.2.988 broken-links --check-anchors`.
- [ ] Preview rendered Mintlify page and confirm image and link appearance.
- [ ] Obtain explicit owner approval before merging, since merging to main can deploy Mintlify.

No P4 command, application build, native test, desktop interaction, or Mintlify CLI was run in this documentation pass.
