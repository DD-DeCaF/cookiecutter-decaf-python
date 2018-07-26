===============================
{{ cookiecutter.project_name }}
===============================

.. image:: https://img.shields.io/pypi/v/{{cookiecutter.project_slug}}.svg
    :target: https://pypi.python.org/pypi/{{cookiecutter.project_slug}}
    :alt: Latest PyPI Version

.. image:: https://img.shields.io/travis/{{cookiecutter.github_account}}/{{cookiecutter.project_slug}}.svg
    :target: https://travis-ci.org/{{cookiecutter.github_account}}/{{cookiecutter.project_slug}}
    :alt: Travis CI

.. image:: https://readthedocs.org/projects/{{cookiecutter.project_slug}}/badge/?version=latest
    :target: https://{{cookiecutter.project_slug}}.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. summary-start

{{cookiecutter.project_short_description}}

Getting Started
===============

From a Python environment you can easily 

.. code-block:: console

    $ pip install {{cookiecutter.project_slug}}

.. summary-end

You can find the full documentation at https://{{cookiecutter.project_slug}}.readthedocs.io.

ToDo
====

Before doing much else you should go through the following steps to fully enable
all the testing goodies of this repository:

* Create a `GitHub <https://github.com/>`_ account and import your local
  repository.
* Create an account at `Read the Docs <https://readthedocs.org>`_ import your
  `GitHub repository`_ there and install the webhook on it.
* Create a `Travis-CI <https://travis-ci.org/>`_ account and enable the
  `GitHub repository`_.

.. _`GitHub repository`: https://github.com/{{cookiecutter.github_account}}/{{cookiecutter.project_slug}}

Copyright
=========

* Copyright (c) {{cookiecutter.year}} {{cookiecutter.full_name}} licensed
  under the `Apache License, Version 2.0 <LICENSE>`_

Credits
=======

This package was created with cookiecutter_ and the `biosustain/cookiecutter-decaf-python`_ project template.

.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _`biosustain/cookiecutter-decaf-python`: https://github.com/biosustain/cookiecutter-decaf-python
