============
Installation
============

Dependencies
------------

`Python`_ 3.7 or later is required. `Anaconda Distribution`_ is
recommended for new starters, it includes Python and few useful packages
including a package manager ``pip`` and built-in virtual environment 
manager.

`pip`_ is a package management system for installing and updating Python
packages. pip comes with Python, so you get pip simply by installing
Python. On Ubuntu and Fedora Linux, you can simply use your system
package manager to install the ``python3-pip`` package. `The
Hitchhiker’s Guide to Python`_ provides some guidance on how to install
Python on your system if it isn’t already; you can also install Python
directly from `python.org`_. You might want to `upgrade pip`_ before
using it to install other programs.

Third party libraries ``numpy``, ``scipy``, ``pandas`` etc. are used in 
``sfeprapy`` and they should be automatically installed behind the scene
if ``pip`` is used for installation. These packages will need to be
installed manually if running directly from source, see requirments.txt
for dependencies.

``pip`` install
---------------

1. to use ``pip`` install from PyPI:

   .. code:: sh

      pip install --upgrade sfeprapy

2. or get the most recent version under developemnt from ``GitHub`` (requires `git`_):

   .. code:: sh

      pip install --upgrade "git+https://github.com/fsepy/sfeprapy.git@dev"

Local install
-------------

`Clone`_ or download (`master`_, `dev`_) ``sfeprapy`` source code from GitHub, unzip and ``cd`` to the source code directory then install using ``pip``:

.. code:: sh

   pip install .

Test installation
-----------------

Upon successful installation of ``sfeprapy``, enter Python and check whether ``sfeprapy`` is installed properly:

.. code-block:: python

   import sfeprapy
   print(sfeprapy.__version__)
   0.8.1

.. _Python: https://www.python.org/downloads/
.. _Anaconda Distribution: https://www.anaconda.com/distribution/#download-section
.. _pip: https://pypi.org/
.. _The Hitchhiker’s Guide to Python: https://docs.python-guide.org/starting/installation/
.. _python.org: https://www.python.org/getit/
.. _upgrade pip: https://pip.pypa.io/en/stable/installing/
.. _git: https://git-scm.com/downloads
.. _multiprocessing: https://docs.python.org/3.4/library/multiprocessing.html#module-multiprocessing
.. _Clone: https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository
.. _master: https://github.com/fsepy/SFEPRAPY/archive/refs/heads/master.zip
.. _dev: https://github.com/fsepy/SFEPRAPY/archive/refs/heads/dev.zip
