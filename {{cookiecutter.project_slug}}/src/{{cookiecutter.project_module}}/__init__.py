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

"""{{cookiecutter.project_short_description}}"""

from __future__ import absolute_import

__author__ = '{{ cookiecutter.full_name }}'
__email__ = '{{ cookiecutter.email }}'
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from {{cookiecutter.project_module}}.utils import *