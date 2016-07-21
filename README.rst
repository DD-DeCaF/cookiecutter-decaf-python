======================
Cookiecutter for python development within DD-DeCaF
======================

|travis|

Cookiecutter_ template for a python package. 

.. |travis| image:: http://img.shields.io/travis/DD-DeCaF/cookiecutter-decaf-python/master.svg?style=flat&label=Travis
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/DD-DeCaF/cookiecutter-decaf-python

.. contents:: Table of Contents

Features
--------

This is a python package cookiecutter template intended for all python
development at the `center for biosustainability
<http://biosustain.dtu.dk>`_ (near copy of the `cookiecutter-pypackage
<https://github.com/audreyr/cookiecutter-pypackage>`_). Using this
template, it is easy to get your project setup for using

* Tox_ for managing test environments for different versions of Python.
* Travis-CI_ and AppVeyor_ for continuous testing.
  * All pushes are triggers testing and tagged pushes to master triggers upload to PyPI
* Coveralls_ or for coverage tracking (using Tox_).
* Documentation with Sphinx_, ready for ReadTheDocs_.
* Easy version tagging with bumpversion_
* Packaging and code quality checks. This template comes with a tox
  environment (``check``) that will:
  * Check if your ``README.rst`` is valid.
  * Check if the ``MANIFEST.in`` has any issues.
  * Run ``flake8`` (a combo of PEP8, pyflakes and McCabe checks) and
    pydocstyle_

The only differences to cookiecutter-pypackage is the addition of

* (optional) use of testing and deployment with AppVeyor
* mandatory use of unit-testing (with pytest)
* support github organizations


Requirements
------------

Projects using this template have these minimal dependencies:

* Cookiecutter_ - just for creating the project
* Tox_ - for running the tests
* Setuptools_ - for building the package, wheels etc. 

To get quickly started on a new system, just `install setuptools
<https://pypi.python.org/pypi/setuptools#installation-instructions>`_ and then `install pip
<https://pip.pypa.io/en/latest/installing.html>`_. That's the bare minimum to required install Tox_ and Cookiecutter_. To install
them, just run this in your shell or command prompt::

  pip install tox cookiecutter

Usage and options
-----------------

First generate your project::

  cookiecutter gh:dd-decaf/cookiecutter-decaf-python

You will be asked for a number of different items, including if you
want to use continuous integration (travis / appveyor), code coverage
etc. If you create many new packages you may consider adding defaults
in ``~/.cookiecutterrc``.

After this you can create the initial repository (make sure you
`create <https://github.com/new>`_ an *empty* Github project)::

  git init .
  git add .
  git commit -m "Initial skel."
  git remote add origin git@github.com:<organization/user>/<new package>.git
  git push -u origin master

Then:

* `Enable the repository in your Travis CI account <https://travis-ci.org/profile>`_.
* `Enable the repository in your codecov account <https://codecov.io/>`_.
* `Add the repo to your ReadTheDocs account
  <https://readthedocs.org/dashboard/import/>`_ + turn on the
  ReadTheDocs service hook. Don't forget to enable virtualenv and
  specify ``docs/requirements.txt`` as the requirements file in
  `Advanced Settings`.

Developing the project
``````````````````````

To run all the tests, just run::

  tox

To make the documentation::

  make docs

To build and verify that the built package is proper and other code QA checks::

  make check

Releasing the project
`````````````````````

Before relasing a new version, we need to increment the version number
and that is done easily using bumpversion_. It's as simple as running:

* ``bumpversion patch`` to increase version from `1.0.0` to `1.0.1`.
* ``bumpversion minor`` to increase version from `1.0.0` to `1.1.0`.
* ``bumpversion major`` to increase version from `1.0.0` to `2.0.0`.

Which will also make the commit and the appropriate git tag.

After incrementing the version, but before creating a new release,
check that the package tests correctly::

    tox

**If you don't use Travis/AppVeyor:** build the ``sdist``, and if
 possible, the ``bdist_wheel`` too::

    python setup.py clean --all sdist bdist_wheel

And then to make a release of the project on PyPI, we upload the
created distribution files using `twine
<https://pypi.python.org/pypi/twine>`_::

    twine register dist/*
    twine upload --skip-existing dist/*

**If you do use Travis/AppVeyor:** Simply make a release by pushing the new tag::

    git push -t <new version>

Which should trigger testing and deployment to PyPI.

.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/
.. _Setuptools: https://pypi.python.org/pypi/setuptools
.. _Pytest: http://pytest.org/
.. _AppVeyor: http://www.appveyor.com/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _bumpversion: https://pypi.python.org/pypi/bumpversion
.. _Codecov: http://codecov.io/
.. _pydocstyle: https://github.com/PyCQA/pydocstyle
