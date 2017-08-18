{% set is_open_source = cookiecutter.open_source_license != 'Proprietary' -%}
===============================
{{ cookiecutter.project_name }}
===============================

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_slug }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_slug }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
{%- endif %}

.. image:: https://pyup.io/repos/github/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_slug }}/shield.svg
     :target: https://pyup.io/repos/github/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_slug }}/
     :alt: Updates

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

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
* Create an `AppVeyor <https://ci.appveyor.com/>`_ account and enable the
  `GitHub repository`_.

.. _`GitHub repository`: https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_slug }}

Features
========

* TODO

Credits
=======

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`biosustain/cookiecutter-decaf-python`: https://github.com/biosustain/cookiecutter-decaf-python
