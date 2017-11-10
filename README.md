# DES Colors

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