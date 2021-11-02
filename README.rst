Introduction
============


.. image:: https://readthedocs.org/projects/circuitpython-nvm-helper/badge/?version=latest
    :target: https://circuitpython-nvm-helper.readthedocs.io/
    :alt: Documentation Status


.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/foamyguy/Foamyguy_CircuitPython_nvm_helper/workflows/Build%20CI/badge.svg
    :target: https://github.com/foamyguy/Foamyguy_CircuitPython_nvm_helper/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

Easy interface to store and retrieve objects persisted via NVM


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/foamyguy-circuitpython-nvm-helper/>`_.
To install for current user:

.. code-block:: shell

    pip3 install foamyguy-circuitpython-nvm-helper

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install foamyguy-circuitpython-nvm-helper

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install foamyguy-circuitpython-nvm-helper



Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install nvm_helper

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

.. code:: python

    import foamyguy_nvm_helper as nvm_helper

    nvm_helper.save_data(
        {"name": "nvm_helper", "num": 92, "float": 3.14}, test_run=False, verbose=True
    )
    read_data = nvm_helper.read_data()
    print("read data is:")
    print(read_data)

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/foamyguy/Foamyguy_CircuitPython_nvm_helper/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
