# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 Tim Cocks for foamyguy
#
# SPDX-License-Identifier: MIT

"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    # Community Bundle Information
    name="foamyguy-circuitpython-nvm-helper",
    use_scm_version={
        # This is needed for the PyPI version munging in the Github Actions release.yml
        "git_describe_command": "git describe --tags --long",
        "local_scheme": "no-local-version",
    },
    setup_requires=["setuptools_scm"],
    description="Easy interface to store and retrieve objects persisted via NVM",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    # The project's main homepage.
    url="https://github.com/foamyguy/Foamyguy_CircuitPython_nvm_helper.git",
    # Author details
    author="Tim Cocks",
    author_email="",  # TODO: Add your email here
    install_requires=[
        "Adafruit-Blinka",
    ],
    # Choose your license
    license="MIT",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Hardware",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    # What does your project relate to?
    keywords="adafruit blinka circuitpython micropython nvm_helper nvm storage",
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # TODO: IF LIBRARY FILES ARE A PACKAGE FOLDER,
    #       CHANGE `py_modules=['...']` TO `packages=['...']`
    py_modules=["foamyguy_nvm_helper"],
)
