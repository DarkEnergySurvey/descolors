# DES Colors

[![Build](https://img.shields.io/travis/kadrlica/descolors.svg)](https://travis-ci.org/kadrlica/descolors)
[![PyPI](https://img.shields.io/pypi/v/descolors.svg)](https://pypi.python.org/pypi/descolors)
[![Release](https://img.shields.io/github/release/kadrlica/descolors.svg)](../../releases)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](../../)

Standard color scheme for plotting DES/DECam filters.

# Installation

The easiest way to install is with `pip`:
```
pip install descolors
```

# Usage

An example usage is
```
from descolors import BAND_COLORS

for k,v in BAND_COLORS.items():
    print('band = %s : color = %s'%(k,v))
```