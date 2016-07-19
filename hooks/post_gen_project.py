#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    if '{{ cookiecutter.use_pypi_deployment_with_travis }}' != 'y':
        remove_file('travis_pypi_setup.py')
    else:
        print(" run python travis_pypi_setup.py after you setup the github repository ")

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if '{{ cookiecutter.use_appveyor }}' != 'y':
        remove_file('appveyor.yaml')

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    print(" {{ cookiecutter.project_name }} generated. Consider ")
    print(" - creating corresponding github repository and then ")
    print(("   git remote add origin git@github.com:"
           "{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git "))
    print(" - instructing travis to build your project ")
