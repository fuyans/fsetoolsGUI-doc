# Release Note

This file documents the release history of `fsetoolsgui`.

## Version History

### XX/XX/2022 VERSION X.X.X

For future development. ☐ incomplete; ☑ completed.

- ☐ **New** `EN1993ExtColWidget` BS EN 1993-1-2 external column temperature.
- ☐ **New** `EN1993ExtBeamWidget` BS EN 1993-1-2 external beam temperature.
- ☐ **New** `SafirStruct3DPostWidget` SAFIR Struct3d Post Processor Strain, converted from previous version.
- ☐ **New** Redo and Undo.
- ☐ **Optim.** B101 Node Table to add import and export.
- ☐ **Misc.** Monetization.

### 07/01/2022 VERSION 0.1.2

- ☑ **New** Distribute horizontally and vertically.
- ☑ **Fix** `DistSelectorWidget` fixed plot does not show up in *0.1.1*.
- ☑ **Optim.** Migrated to Qt6 (from Qt5).
- ☑ **Optim.** New custom plot module based on `Qt.QtCharts` replacing `pyqtgraph`.

### 02/01/2022 VERSION 0.1.1

- ☑ **New** Integrated B101 module for exit capacity calculation and visualisation.
- ☑ **New** NodeList B101 Node Table to enhance efficiency editing/reviewing B101 nodes and their values.
    - ☑ Dedicated `QDialog` UI.
    - ☑ Update the item in the Table upon changes made in the View/Scene.
    - ☑ Update the item in the View/Scene upon changes made in the Table.
    - ☑ Centre item in the View upon select in the Table.
    - ☑ Remove items in the View/Scene also remove in the Table.
- ☑ **New** `PRAPostFireWidget` migrated from previous version.
- ☑ **Fix** Fixed B101 nodes horizontal and vertical alignment issues due to double counting item geometry.

### 16/12/2021 VERSION 0.1

- ☑ **New** Refreshed user interface.
- ☑ **New** Added save and load feature.
- ☑ **New** `PRAPostFireWidget` migrated from previous version.
- ☑ **New** `BR187PerpendicularRoofWidget` migrated from previous version.
- ☑ **New** `StefanBoltzmannLawWidget`.
- ☑ **New** `ImageWidget`.
- ☑ **New** `FDSMeshMPIOptimWidget`.
- ☑ **New** `ExternalModuleWidget`.
- ☑ **New** `BR187SummaryWidget`.
- ☑ **New** `BR187PerpendicularWallWidget`.
- ☑ **New** `FSEKitchenHobWidget`.
- ☑ **New** macOS support.

### 04/09/2021 VERSION: 0.0.9

This is an accumulated node since 0.0.4.

- ☑ **New** FDS mesh mpi optimiser.
- ☑ **New** Probability distribution.
- ☑ **New** `ISO834FireWidget` ISO 834 fire.
- ☑ **New** `PRAPreWidget` SFEPRAPY pre-processor.
- ☑ **New** `PRAProcWidget` SFEPRAPY processor.
- ☑ **New** `PRAPostWidget` SFEPRAPY post-processor.
- ☑ **Fix** `PD7974HDActWidget` PD 7974 heat detector device activation time, fixed incorrect image being displayed.

### 16/06/2020 VERSION: 0.0.4

- ☑ **New** 0103 BS 9999 merging flow at final exit level.
- ☑ **New** 0104 ADB merging flow at final exit level.
- ☑ **New** 0407 TRA cuboid enclosure model.
- ☑ **New** 0611 EC 1991-1-2 parametric fire generator.
- ☑ **Fix** Fixed an issue where the update download url label no responses when clicked.
- ☑ **Improve** 0401, 0402, 0403 & 0404: Added critical heat flux input parameter.
- ☑ **Improve** Installer: Interface optimisation.

### 14/02/2020 VERSION: 0.0.1

- ☑ 0101 ADB data sheet.
- ☑ 0102 BS 9999 data sheet.
- ☑ 0111 PD 7974 heat detector activation time.
- ☑ 0401 BR 187 parallel simple.
- ☑ 0402 BR 187 perpendicular simple.
- ☑ 0403 BR 187 parallel complex.
- ☑ 0404 BR 187 perpendicular complex.
- ☑ 0405 general thermal radiation analysis.
- ☑ 0601 OFR naming.
- ☑ 0602 PD 7974 flame height.
- ☑ 0111 implemented display numerical results in the table.
- ☑ 0111 implemented graphical output.
- ☑ Converted all independent modules into QMainWindow objects, i.e. to have a status bar.
- ☑ Installer for MS Windows.
- ☑ All output files are set to read only.
- ☑ Shortcut for all module GUI windows press ESC to close.
- ☑ Implemented error handling.
- ☑ Implemented check GUI tip texts.

## Checklist before release

1. Update version number `fsetoolsGUI.project_info.__version__`.
2. Build executable using pyinstaller (make sure unnecessary files are removed).
3. Build NSIS installer.
4. Install and test the program:
    1. The previous version uninstalls successfully.
    2. Test b101.fselic.
    3. Load `v_fsetoolsGUI\calc\all.fse` without issues.
    4. Load `v_fsetoolsGUI\b101\std.fse` and run Flow without issues.
    5. Save without issues.
5. Update remote update file as necessary.
6. Update doc as necessary.
7. Commit and pull to master.
