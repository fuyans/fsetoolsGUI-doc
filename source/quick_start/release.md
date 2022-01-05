# Release

This file documents the release history of `fsetoolsgui`.

## Version History

### XX/XX/2022 VERSION X.X.X:

For future development.

- [ ] \[New\] `EN1993ExtColWidget` BS EN 1993-1-2 external column temperature
- [ ] \[New\] `EN1993ExtBeamWidget` BS EN 1993-1-2 external beam temperature
- [ ] \[New\] `SafirStruct3DPostWidget` SAFIR Struct3d Post Processor Strain, converted from previous version.
- [ ] \[New\] Redo and Undo.
- [ ] \[New\] Monetization.
- [ ] \[Optim.\] Migrate to Qt6 (from Qt5).

### XX/01/2022 VERSION 0.1.2:

- [x] \[Optim.\] New custom plot module based on Qt.QtCharts replacing `pyqtgraph`.

### 02/01/2022 VERSION 0.1.1:

- [x] \[New\] Integrated B101 module for exit capacity calculation and visualisation.
- [x] \[New\] NodeList B101 Node Table to enhance efficiency when assign/inspect B101 nodes and their values.
    - [x] Dedicated `QDialog` UI.
    - [x] Update the item in the Table upon changes made in the View/Scene.
    - [x] Update the item in the View/Scene upon changes made in the Table.
    - [x] Centre item in the View upon select in the Table.
    - [x] Remove items in the View/Scene also remove in the Table.
- [x] \[New\] `PRAPostFireWidget` migrated from previous version.
- [x] \[Fix\] Fixed B101 nodes horizontal and vertical alignment issues due to double counting item geometry.

### 16/12/2021 VERSION 0.1:

- [x] \[New\] Refreshed user interface.
- [x] \[New\] Added save and load feature.
- [x] \[New\] `PRAPostFireWidget` migrated from previous version.
- [x] \[New\] `BR187PerpendicularRoofWidget` migrated from previous version.
- [x] \[New\] `StefanBoltzmannLawWidget`.
- [x] \[New\] `ImageWidget`.
- [x] \[New\] `FDSMeshMPIOptimWidget`.
- [x] \[New\] `ExternalModuleWidget`.
- [x] \[New\] `BR187SummaryWidget`.
- [x] \[New\] `BR187PerpendicularWallWidget`.
- [x] \[New\] `FSEKitchenHobWidget`.
- [x] \[New\] macOS 🖥 support.

### 04/09/2021 VERSION: 0.0.9

This is an accumulated node since 0.0.4.

- [x] \[New\] FDS mesh mpi optimiser.
- [x] \[New\] Probability distribution.
- [x] \[New\] `ISO834FireWidget` ISO 834 fire.
- [x] \[New\] `PRAPreWidget` SFEPRAPY pre-processor.
- [x] \[New\] `PRAProcWidget` SFEPRAPY processor.
- [x] \[New\] `PRAPostWidget` SFEPRAPY post-processor.
- [x] \[Fix\] `PD7974HDActWidget` PD 7974 heat detector device activation time, fixed incorrect image being displayed.

### 16/06/2020 VERSION: 0.0.4

- [x] \[New\] 0103 BS 9999 merging flow at final exit level.
- [x] \[New\] 0104 ADB merging flow at final exit level.
- [x] \[New\] 0407 TRA cuboid enclosure model.
- [x] \[New\] 0611 EC 1991-1-2 parametric fire generator.
- [x] \[Fix\] Fixed an issue where the update download url label no responses when clicked.
- [x] \[Improve\] 0401, 0402, 0403 & 0404: Added critical heat flux input parameter.
- [x] \[Improve\] Installer: Interface optimisation.

### 14/02/2020 VERSION: 0.0.1

- [x] 0101 ADB data sheet.
- [x] 0102 BS 9999 data sheet.
- [x] 0111 PD 7974 heat detector activation time.
- [x] 0401 BR 187 parallel simple.
- [x] 0402 BR 187 perpendicular simple.
- [x] 0403 BR 187 parallel complex.
- [x] 0404 BR 187 perpendicular complex.
- [x] 0405 general thermal radiation analysis.
    - [x] Calculation checked.
- [x] 0601 OFR naming.
- [x] 0602 PD 7974 flame height.
    - [x] Calculation checked.
- [x] 0111 implemented display numerical results in the table.
- [x] 0111 implemented graphical output.
- [x] Converted all independent modules into QMainWindow objects, i.e. to have a status bar.
- [x] Installer for MS Windows.
- [x] All output files are set to read only.
- [x] Shortcut for all module GUI windows press ESC to close.
- [x] Implemented error handling.
- [x] Implemented check GUI tip texts.

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
