Version
=======

Version is displayed at the bottom of the `FSETools`'s main window. It consists of three integers separated by dot :code:`major`.\ :code:`minor`.\ :code:`patch`. Build information is also implemented in-addition to Version which is essentially the date and time when the source code is being compiled. This is primarily used for debugging purposes where multiple Build may present for testing under the same Version.

`FSETools` implements an update checker module which is called upon execution of the app.


Update
======

Check update successful
-----------------------

Check update status is indicated in the Version text colour located at the bottom of the main window. Grey colour means that the update check has completed successfully and there is no updates available.

.. figure:: /quick_start/update/check-update-successful.png
    :alt: figure missing, check-update-successful.png

Check update failed
-------------------

Following above, Black colour means the check update process is failed. A common cause is there is no internet access or failed to reach the update info server.

.. figure:: /quick_start/update/check-update-failed.png
    :alt: image is missing, check-update-failed.png

Error message can be found in the :code:`FSETools Logbook` applet.

.. figure:: /quick_start/update/check-update-failed-log.png
    :alt: image is missing, check-update-failed-log.png

New version available
---------------------

Where there are new versions available to install, a message will be shown at the bottom of the main window.

.. figure:: /quick_start/update/check-update-new-version-available.png
    :alt: figure missing, check-update-new-version-available.png

Current version disabled
------------------------

In certain circumstances where the current running version could be disabled due to various reasons, e.g. a critical bug had been identified, all applets will be set to inaccessible and update to the latest version is mandatory.

.. figure:: /quick_start/update/check-update-current-version-disabled.png
    :alt: figure missing, check-update-current-version-disabled.png
