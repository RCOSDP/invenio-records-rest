# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Python 2/3 compatibility helpers."""

try:  # Python 3 way of inspecting functions
    from inspect import signature, Parameter

    def wrap_links_factory(links_factory):
        """Test if the links_factory function accepts kwargs."""
        sign = signature(links_factory)
        kwargs_param = [p for p in sign.parameters.values()
                        if p.kind == Parameter.VAR_KEYWORD]
        return len(kwargs_param) == 0
except ImportError:  # Python 2 way of inspecting functions
    from inspect import getargspec

    def wrap_links_factory(links_factory):
        """Test if the links_factory function accepts kwargs."""
        spec = getargspec(links_factory)
        return spec.keywords is None
