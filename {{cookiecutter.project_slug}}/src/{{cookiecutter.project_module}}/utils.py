# -*- coding: utf-8 -*-

# Copyright (c) {{ cookiecutter.year }} {{ cookiecutter.full_name }}
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Provide general utility functions."""

from __future__ import absolute_import

from depinfo import print_dependencies


__all__ = ("show_versions",)


def show_versions():
    """Print system and Python environment dependency information."""
    print_dependencies("{{cookiecutter.project_slug}}")
