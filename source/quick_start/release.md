# Release Note

This file documents the release history of `fsetoolsgui`.

## Known Issues

- macOS. Warning message upon instantiation of `CalculationNode`:  
  `qt.qpa.fonts: Populating font family aliases took 370 ms. Replace uses of missing font family "Menlo" with one that exists to avoid this cost. `
- macOS. Warning messages when `QGraphicsView` gain/lose focus:  
  `qt.pointer.dispatch: delivering touch release to same window QWindow(0x0) not QWidgetWindow(0x600000952f40, name="MainWindowClassWindow")`  
  `qt.pointer.dispatch: skipping QEventPoint(id=1 ts=0 pos=0,0 scn=816.915,868.501 gbl=816.915,868.501 Released ellipse=(1x1 ∡ 0) vel=0,0 press=-816.915,-868.501 last=-816.915,-868.501 Δ 816.915,868.501) : no target window`  
  See https://bugreports.qt.io/browse/QTBUG-95887 and https://bugreports.qt.io/browse/QTBUG-88192.

## Version History

### XX/XX/2022 VERSION X.X.X

For future development. ☐ incomplete; ☑ completed.

- ☐ **New** `EN1993ExtColWidget` BS EN 1993-1-2 External Column temperature.
- ☐ **New** `EN1993ExtBeamWidget` BS EN 1993-1-2 External Beam temperature.
- ☐ **New** `SafirStruct3DPostWidget` SAFIR Struct3d Post Processor Strain, converted from previous version.
- ☐ **New** Redo and Undo.
- ☐ **Fix** Crash upon close, particularly when items are deleted.
- ☐ **Optim.** `ProbDistWidget` export CSV with constant CDF interval.
- ☐ **Optim.** B101 Node Table to add import and export.

### XX/XX/2022 VERSION 0.1.3

- ☑ **Fix** Fixed crash upon exit the application due to double `QGraphicsScene.removeItem` performed upon same item.
- ☑ **Optim.** Import Images now use `ImageNode` instead of `ImageWidget`.

### 07/01/2022 VERSION 0.1.2

- ☑ **New** Distribute horizontally and vertically.
- ☑ **Fix** `DistSelectorWidget` fixed plot does not show up in *0.1.1*.
- ☑ **Fix** `ImageNode` fixed crash when image scaled up more than 300 %.
- ☑ **Optim.** Migrated to Qt6 (from Qt5).
- ☑ **Optim.** New custom plot module based on `Qt.QtCharts` replacing `pyqtgraph`.

### 02/01/2022 VERSION 0.1.1

- ☑ **New** Integrated B101 module for exit capacity calculation and visualisation.
- ☑ **New** NodeList B101 Node Table to enhance efficiency editing/reviewing B101 nodes and their values.
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

Cumulative since 0.0.4. Module ID is depreciated from 0.0.9 and onwards.

- ☑ **New** `ProbDistWidget` FDS mesh MPI optimiser.
- ☑ **New** `ProbDistWidget` Probability distribution.
- ☑ **New** `ISO834FireWidget` ISO 834 fire.
- ☑ **New** `PRAPreWidget` SFEPRAPY pre-processor.
- ☑ **New** `PRAProcWidget` SFEPRAPY processor.
- ☑ **New** `PRAPostWidget` SFEPRAPY post-processor.
- ☑ **Fix** `PD7974HDActWidget` PD 7974 heat detector device activation time, fixed incorrect image being displayed.

### 16/06/2020 VERSION: 0.0.4

Cumulative since 0.0.1.

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
- ☑ 0111 implemented display numerical results in a table.
- ☑ 0111 implemented graphical (plot) output.
- ☑ Converted all independent modules into QMainWindow objects, i.e. to have a status bar.
- ☑ Installer for MS Windows.
- ☑ All output files are set to read only.
- ☑ Shortcut for all module GUI windows press ESC to close.
- ☑ Implemented error handling.
- ☑ Implemented check GUI tip texts.

## Checklist before release

1. Update version number `fsetoolsGUI.project_info.__version__`.
2. Build executable (make sure unnecessary files are removed).
3. Build installer. Install and test the program:
    1. To check whether the previous version uninstalls successfully.
    2. Test `b101.fselic`.
    3. Load `v_fsetoolsGUI\calc\all.fse` without issues.
    4. Load `v_fsetoolsGUI\b101\std.fse` and run Flow without issues.
    5. Save without issues.
4. Update remote update file as necessary.
5. Update doc as necessary.
6. Commit and pull to master.
