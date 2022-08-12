# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

from docutils.parsers.rst import directives, roles, nodes
import re

LIB_REGEX = re.compile('gf180mcu_(?P<lib_src>[^_\s]*)_(?P<lib_type>[^_\s]*)(_(?P<lib_name>[^_\s]*))?')
CELL_REGEX = re.compile('gf180mcu_(?P<lib_src>[^_\s]*)_(?P<lib_type>[^_\s]*)(_(?P<lib_name>[^_\s]*))?__(?P<cell_name>[^\s]*)')

def lib_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Library name which gets colorized."""
    m = LIB_REGEX.match(text)
    if not m:
        msg = inliner.reporter.error("Malformed library name of "+repr(text), line=lineno)
        prb = inliner.problematic(rawtext, rawtext, msg)
        return [prb], [msg]
    app = inliner.document.settings.env.app

    lib_process = 'gf180mcu'
    lib_src = m.group('lib_src')
    lib_type = m.group('lib_type')
    lib_name = m.group('lib_name')

    r = [
        nodes.inline(lib_process, lib_process, classes=['lib-process']),
        nodes.inline('_', '_', options=options),
        nodes.inline(lib_src, lib_src, classes=['lib-src']),
        nodes.inline('_', '_', options=options),
        nodes.inline(lib_type, lib_type, classes=['lib-type']),
    ]
    if lib_name:
        r.append(nodes.inline('_', '_', options=options))
        r.append(nodes.inline(lib_name, lib_name, classes=['lib-name']))

    return r, []


def cell_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Cell name which gets colorized."""
    m = CELL_REGEX.match(text)
    if not m:
        msg = inliner.reporter.error("Malformed cell name of "+repr(text), line=lineno)
        prb = inliner.problematic(rawtext, rawtext, msg)
        return [prb], [msg]
    app = inliner.document.settings.env.app

    lib_process = 'gf180mcu'
    lib_src = m.group('lib_src')
    lib_type = m.group('lib_type')
    lib_name = m.group('lib_name')
    cell_name = m.group('cell_name')

    r = [
        nodes.inline(lib_process, lib_process, classes=['lib-process']),
        nodes.inline('_', '_', options=options),
        nodes.inline(lib_src, lib_src, classes=['lib-src']),
        nodes.inline('_', '_', options=options),
        nodes.inline(lib_type, lib_type, classes=['lib-type']),
    ]
    if lib_name:
        r.append(nodes.inline('_', '_', options=options))
        r.append(nodes.inline(lib_name, lib_name, classes=['lib-name']))
    r.append(nodes.inline('__', '__', options=options))
    r.append(nodes.inline(cell_name, cell_name, classes=['cell-name']))

    return r, []


def add_role(app, new_role_name):
    options = {
        'class': directives.class_option(new_role_name),
    }
    role = roles.CustomRole(new_role_name, roles.generic_custom_role, options, "")
    app.add_role(new_role_name, role)


def setup(app):
    app.add_css_file('extra.css')
    add_role(app, 'cell_name')
    add_role(app, 'lib_process')
    add_role(app, 'lib_src')
    add_role(app, 'lib_type')
    add_role(app, 'lib_name')
    add_role(app, 'drc_rule')
    add_role(app, 'drc_tag')
    add_role(app, 'drc_flag')
    add_role(app, 'layer')

    app.add_role('lib', lib_role)
    app.add_role('cell', cell_role)
    app.add_role('model', cell_role)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

