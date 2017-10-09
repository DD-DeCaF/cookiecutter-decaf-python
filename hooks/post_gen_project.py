#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

import sys
from os import remove
from os.path import join, realpath, curdir

PROJECT_DIRECTORY = realpath(curdir)


def remove_file(filename):
    try:
        remove(join(PROJECT_DIRECTORY, filename))
    except OSError as err:
        print(str(err), file=sys.stderr)


if __name__ == '__main__':
    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if '{{ cookiecutter.use_appveyor }}' != 'y':
        remove_file('appveyor.yaml')

    if '{{ cookiecutter.open_source_license }}' == 'Proprietary':
        remove_file('LICENSE')

    print("\n\n {{ cookiecutter.project_name }} generated. Consider ")
    print(" - creating the corresponding github repository and then ")
    print(("   git remote add origin git@github.com:"
           "{{ cookiecutter.github_organization }}/{{ cookiecutter.project_slug }}.git "))
    print("   git push -u origin master ")
    if '{{ cookiecutter.use_pypi_deployment_with_travis }}' != 'y':
        remove_file('travis_pypi_setup.py')
    else:
        print((" - instructing travis to build your project and then running\n"
               "   python travis_pypi_setup.py\n"
               "   after you setup the github repository"))
    if '{{ cookiecutter.use_pypi_deployment_with_appveyor }}' == 'y':
        pass
        print((" - instructing appveyor to build your project and then\n"
               "   updating the encrypted pypi password in appveyor.yml\n"))
    print("\n\n")

