CrowconTempIOC
===========================

|code_ci| |docs_ci| |coverage| |pypi_version| |license|

Code to read three temperatures from a Crowcon device and output to an IOC.
The temperatures read are Warm Base, Cold Chuck and Gripper BB.
This code is a work in progress and does not currently function.

============== ==============================================================
PyPI           ``pip install CrowconTempIOC``
Source code    https://github.com/8ryn/CrowconTempIOC
Documentation  https://8ryn.github.io/CrowconTempIOC
Releases       https://github.com/8ryn/CrowconTempIOC/releases
============== ==============================================================

Should be able to be launched from the command line as::

    $ python -m CrowconTempIOC --url url_to_load

If not given a url option progam currently defaults to http://127.0.0.1:5000

.. |code_ci| image:: https://github.com/8ryn/CrowconTempIOC/actions/workflows/code.yml/badge.svg?branch=main
    :target: https://github.com/8ryn/CrowconTempIOC/actions/workflows/code.yml
    :alt: Code CI

.. |docs_ci| image:: https://github.com/8ryn/CrowconTempIOC/actions/workflows/docs.yml/badge.svg?branch=main
    :target: https://github.com/8ryn/CrowconTempIOC/actions/workflows/docs.yml
    :alt: Docs CI

.. |coverage| image:: https://codecov.io/gh/8ryn/CrowconTempIOC/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/8ryn/CrowconTempIOC
    :alt: Test Coverage

.. |pypi_version| image:: https://img.shields.io/pypi/v/CrowconTempIOC.svg
    :target: https://pypi.org/project/CrowconTempIOC
    :alt: Latest PyPI version

.. |license| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
    :target: https://opensource.org/licenses/Apache-2.0
    :alt: Apache License

..
    Anything below this line is used when viewing README.rst and will be replaced
    when included in index.rst

See https://8ryn.github.io/CrowconTempIOC for more detailed documentation.
