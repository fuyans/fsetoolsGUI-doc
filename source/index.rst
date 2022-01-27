######################
FSETools Documentation
######################

Introduction
============

FSETools compiles several Fire Safety Engineering tools. Mostly based on contemporary guidance documents (e.g. ADB /
BS 9999 / BS 7974). Users are expected to have a thorough understanding of the methodologies behind these tools.

Main Window Layout
------------------

A good picture worth thousands words.

.. _fig-main-window-layout:

.. figure:: /quick_start/main-window-layout.png

    A sketch of the main window layout of FSETools

.. _table-main-window-components:

.. list-table:: Main UI components
    :widths: 10 90
    :header-rows: 1

    * - Component
      - Description
    * - Frame
      - The topmost bar of the main window housing title and min/max/exit buttons.
    * - Menu Bar
      - A horizontally oriented menu bar housing all options in form of dropdown menus.
    * - Side Menu
      - A vertically oriented tree menu housing shortcut for activating useful tools (also see
        :ref:`section-calculation-node-layout`).
    * - Viewport
      - A viewport area allows the users to see calculation inputs and outputs etc. Can be toggled visible/hidden by
        View -> Side Menu.
    * - Console
      - A command-line style area to display various information, e.g. calculation errors/warnings etc. Can be toggled
        visible/hidden by View -> Console.
    * - Status Bar
      - The bottom bar of the main window. The last line in the Console will be displayed on this bar for 5 seconds.
        Version info, viewport location and zoom are displayed on the right end (click these text to reveal extra
        info/options).

.. _section-calculation-node-layout:

Calculation Node Layout
-----------------------

Most of the calculation modules hosted within the Side Menu (see :numref:`fig-main-window-layout`) share a common
layout as per :numref:`fig-common-calculation-node-layout` for consistency.

.. _fig-common-calculation-node-layout:

.. figure:: /quick_start/common-calc-node-layout.png
    :width: 500px

    A sketch of Calculation Node common layout

Keyboard Shortcuts
==================

.. _table-keyboard-shortcuts:

.. list-table:: Keyboard shortcuts
    :widths: 30 70
    :header-rows: 1

    * - Shortcut
      - Effect
    * - Ctrl + A
      - Select all items
    * - Ctrl + C
      - Copy selected item(s)
    * - Ctrl + V
      - Paste copied item(s)
    * - Del
      - Delete selected item(s)
    * - Ctrl + O
      - Open a saved file
    * - Ctrl + S
      - Save current scene to a file
    * - Ctrl + Shift + S
      - To save current scene to a new file
    * - R
      - To create a Room node. Requires :ref:`section-b101-license`.
    * - D
      - To create a Door node. Requires :ref:`section-b101-license`.
    * - E
      - To create an Exit node. Requires :ref:`section-b101-license`.
    * - S
      - To create a Stair node. Requires :ref:`section-b101-license`.
    * - X
      - To create a X node. Requires :ref:`section-b101-license`.
    * - Ctrl + Shift + R
      - To toggle b101 visualisation. Requires :ref:`section-b101-license`.
    * - Ctrl + R
      - To update b101 flow (also switch on visualisation). Requires :ref:`section-b101-license`.

Mouse Action and Effect
=======================

.. note::
    Most items in :numref:`table-mouse-actions` works only when Viewport is focused. Click any blank area in Viewport
    to gain focus.

.. _table-mouse-actions:

.. list-table:: Mouse actions
    :widths: 30 70
    :header-rows: 1

    * - Action
      - Effect
    * - Left button press
      - To select a single item
    * - Left button hold + move
      - To select multiple items
    * - Right button press
      - To call context menu depending upon selection
    * - Middle button hold + move
      - Move viewport

.. _section-b101-license:

B101 License
============

.. note::
    New in version 0.1.2

B101 is still a work in progress and therefore supplied with limited access. Contact Ian if you are interested in
testing B101 (a 30 minutes training is required for new starters as lack of proper documentation). Upon agreement,
follow the steps below to obtain and install a B101 license file:

1. Click Help -> About to get the specification data displayed in Console, formatted as per below.

    ::

        About FSETools:
        FSETools 0.1.1 202112312253
        Expires in 364 day(s), 2 hour(s) and 9 minute(s)
        UID 00000000-0000-0000-0000-XXXXXXXXXXXX
        Root C:\Program Files (x86)\FSETOOLSGUI

2. Send this information (particularly version and UID) to Ian to request a licence file (named :code:`b101.fselic` and
   do not change this file name).

3. First save the license file :code:`b101.fselic` to an accessible folder (e.g., Desktop or Downloads). Then move the
   file to the root folder (shown in Step 1). This may require administrator access.

Upon completion of the steps above, click View -> B101 Toolbar (or press Ctrl+Shift+Alt+B) to show/activate B101 Toolbar as shown in :numref:`fig-b101-activation` (press again to hide/deactivate). B101 features are only accessible when the toolbar is visible (as well as the keyboard shortcuts in :numref:`table-keyboard-shortcuts`).

.. _fig-b101-activation:

.. figure:: /quick_start/b101-toolbar.png
    :alt: B101 Toolbar

    B101 Toolbar

.. note::
    A license file only works for a specific version on a specific machine, meaning that upgrading FSETools or running the software on a different machine will require a new license file.


Installation
============

Download and execute installer.

.. figure:: /quick_start/install/installer-icon.png
    :alt: Setup: Installer

You may see a pop-up dialog window asking to uninstall previous versions (if exist). After pressed the **Yes** button, wait 10 seconds before move onto the next step for the uninstallation to complete.

.. figure:: /quick_start/install/installer-setup-uninstall-previous.png
    :alt: Setup: Uninstall previous version

Click **Next** to start installation then wait for the installation progress to complete.

.. figure:: /quick_start/install/installer-setup-1.png
    :alt: Setup: Welcome

Installation complete, click **Finish** to close the installer.

.. figure:: /quick_start/install/installer-setup-3.png
    :alt: Setup: Complete

The application should be able to run.

.. figure:: /quick_start/install/start-shortcut.png
    :alt: Setup: FSETools


Update
======

FSETools has builtin check update module. To check for updates, simply click the version text located at the bottom right corner of the main window as per :numref:`fig-check-update`.

.. _fig-check-update:

.. figure:: /quick_start/demo/version.gif
    :alt: Check update

    Check for Updates

Release
=======

.. include:: ./quick_start/release.md
    :parser: myst_parser.sphinx_

.. toctree::
    :maxdepth: 2
    :hidden:

    b1/index.rst
    b3/index.rst
    b4/index.rst
    pra/index.rst
    misc/index.rst
