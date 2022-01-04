######################
FSETools Documentation
######################

Introduction
============

FSETools (also referred to as FSEToolsGUI) compiles several Fire Safety Engineering helper tools that are mostly based on
contemporary guidance documents (e.g. ADB / BS 9999 / BS 7974). FSETools is designed to enhance the efficiency, accuracy
and consistency of the fire engineering design process. Users are expected to have a thorough understanding of the
methodologies behind these tools.

.. figure:: /quick_start/conceptual.png
    :alt: Conceptual sketch main component

.. list-table:: Main UI Components
    :widths: 10 90
    :header-rows: 1

    * - Component
      - Description
    * - Frame
      - The topmost bar of the main window housing title and min/max/exit buttons.
    * - Menu Bar
      - A horizontally oriented menu bar housing all options in form of dropdown menus.
    * - Side Menu
      - A vertically oriented tree menu housing shortcut for summoning useful tools.
    * - Viewport
      - A viewport area allows the users to see calculation inputs and outputs etc. Can be toggled visible/hidden by View -> Side Menu.
    * - Console
      - A command-line style area to display various information, e.g. calculation errors/warnings etc. Can be toggled visible/hidden by View -> Console.
    * - Status Bar
      - The bottom bar of the main window. The last line in the Console will be displayed on this bar for 5 seconds. Version info, viewport location and zoom are displayed on the right end (click these text to reveal extra info/options).

.. figure:: /quick_start/demo/gen.gif
    :alt: gen.gif


Keyboard and Mouse Action and Effect
====================================

.. list-table:: Mouse Action
    :widths: 30 70
    :header-rows: 1

    * - Mouse
      - Effect
    * - Left button press
      - To select a single item
    * - Left button hold + move
      - To select multiple items
    * - Right button press
      - To call context menu depending upon selection
    * - Middle button hold + move
      - Move viewport

.. _table-keyboard-shortcuts:
.. list-table:: Keyboard shortcuts
    :widths: 30 70
    :header-rows: 1

    * - Keyboard
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
      - ``B101`` To create a Room node
    * - D
      - ``B101`` To create a Door node
    * - E
      - ``B101`` To create an Exit node
    * - S
      - ``B101`` To create a Stair node
    * - X
      - ``B101`` To create a X node
    * - Ctrl + Shift + R
      - ``B101`` To toggle b101 visualisation
    * - Ctrl + R
      - ``B101`` To update b101 flow (also switch on visualisation)


Installation
============

Download `FSETOOLSGUI` and double click the installer.

.. figure:: /quick_start/install/installer-icon.png
    :alt: Setup: Installer

You may see a pop-up dialog window asking to uninstall previous versions (if exist). Give it ten seconds after clicking the **Yes** button.

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


B101 License
============

B101 is a work in progress and therefore supplied with limited access to alpha testers. Contact Ian if you are interested in testing B101 (a 30 minutes training is required for new starters). Upon agreement, follow the three simple steps below to obtain and install a B101 license file:

1. Click Help -> About to get specification data displayed in Console. Below shows an example.

    ::

        About FSETools:
        FSETools 0.1.1 202112312253
        Expires in 364 day(s), 2 hour(s) and 9 minute(s)
        UID 00000000-0000-0000-0000-103d1ccd0662
        Root C:\Program Files (x86)\FSETOOLSGUI

2. Send this information (particularly version and UID) to Ian to request a licence file (named :code:`b101.fselic`).

3. First save the license file :code:`b101.fselic` to an accessible folder (e.g., Desktop or Downloads). Then move the file to the root folder (path shown in Step 1).

.. note::
    Step 3 requires administrator access.

Upon completion of the steps above, press Ctrl+Shift+Alt+B to activate B101 toolbar. B101 features will be
accessible when the toolbar is visible (and the keyboard shortcuts in :numref:`table-keyboard-shortcuts`).

.. note::
    A license file only works for a specific version on a specific machine, meaning that upgrading FSETools or running
    the software on a different machine will require a new license file.

.. figure:: /quick_start/b101.png
    :alt: B101 Example


Release
=======

.. include:: /quick_start/release.md
    :literal:


.. toctree::
    :maxdepth: 2
    :hidden:

    b1/index.rst
    b3/index.rst
    b4/index.rst
    pra/index.rst
    misc/index.rst
