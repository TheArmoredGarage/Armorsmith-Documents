# Painting documentation follow-up — November 23, 2026

Target: Armorsmith Designer 2.1.2.0
Status: DRAFT documentation change; preserve the release review gate.

## What changed in this documentation PR

- Updated **Paint materials on a model** to describe the new Brush **Density** and **Sharpness** controls. Clarified that Size scales the whole stamp rather than tiling it, and documented **Load Mask...**.
- Expanded Decal Pass instructions using **Add Decal...**, the decal list, placement and transform actions, projection controls, and **Apply Material To Selected Decal**.
- Removed obsolete guidance about **Show Coverage Preview** from the current Weathering Pass instructions.
- Added **Add black wash and edge wear**, including current effect parameter labels, pass order, and shared **Edge Wear Shaping** controls.
- Updated the beginner painting tutorial and Mintlify's Painting navigation.
- Preserved existing image paths and document routes.

## Evidence

Read-only inspection of application source, including:
- `Code/FE/PaintEditorPanel.h` (Density, Sharpness, brush mode and settings).
- `Code/MeshTools/PaintStampMask.cpp` (single-stamp scale and density-based contour erosion).
- `Code/FE/PaintStampSelector.cpp` (brush presets and Load Mask).
- `Code/FE/ProjectedDecalEditor.cpp` (new decal editor labels).
- `Code/FE/PaintWeatheringPanel.cpp` (Weathering Pass, Black Wash, Edge Wear, Curvature Properties).
- `Code/FE/MaterialPassPanel.cpp` (pass list, ordering and selection).
- The owner's November 23 review accepted the new brush controls and visual direction; that is not a substitute for native release QA.

## Publication checklist

- [ ] Verify the exact 2.1.2.0 release candidate and visible labels. Feature-complete is not the same as published.
- [ ] Confirm 100% Density / 50% Sharpness reproduces the original brush mask. Lower Density should thin existing features rather than randomly erase entire regions; 0% paints nothing.
- [ ] Confirm that Size enlarges one stamp and does not tile.
- [ ] Verify brush hover preview and committed stroke match, particularly for complex masks and Fast/Precise Visibility.
- [ ] Confirm Edge Wear Relative Width, Width Variation, Width Frequency, Chip Size, Chip Amount and asset-wide Edge Wear Shaping in the app.
- [ ] Verify Black Wash remains unchanged from its approved look.
- [ ] Verify **Add Decal...**, placement, ordering, and selected-material application.
- [ ] Save, close, and reopen a four-pass test costume (Paint 1 / Decal / Black Wash / Edge Wear) and compare results.
- [ ] Recheck compatibility with existing development/test costumes saved in last week's material format; a successful current-format round-trip alone is insufficient.
- [ ] Replace the older Brush and Weathering screenshots on a later capture pass: the Brush capture predates Density/Sharpness and the Weathering capture includes an earlier control layout.
- [ ] Run `python -m unittest discover -s tests -p 'test_*.py' -v`.
- [ ] Run `npx --yes mint@4.2.988 validate`.
- [ ] Run `npx --yes mint@4.2.988 broken-links --check-anchors`.
- [ ] Inspect rendered pages at readable size and verify internal links.
- [ ] Obtain owner approval before moving to Ready for Review / merging.

No application builds, runtime tests, CLI validation, or desktop interaction were executed during this documentation update.
