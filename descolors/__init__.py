#!/usr/bin/env python
"""
DES color standards.
"""
__author__ = "Alex Drlica-Wagner"

from collections import OrderedDict as odict
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

__all__ = ['BAND_COLORS']

BAND_COLORS = odict([
    ('u','#56b4e9'),
    ('g','#008060'),
    ('r','#ff4000'),
    ('i','#850000'),
    ('z','#6600cc'),
    ('Y','#000000'),
])
