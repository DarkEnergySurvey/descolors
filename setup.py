import sys
import os
try: from setuptools import setup
except ImportError: from distutils.core import setup
import versioneer

URL = 'https://github.com/kadrlica/descolors'

setup(
    name='descolors',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url=URL,
    author='Alex Drlica-Wagner',
    author_email='kadrlica@fnal.gov',
    scripts = [],
    packages=['descolors'],
    description="Standard color scheme for plotting DES/DECam filters.",
    long_description="See %s"%URL,
    platforms='any',
    keywords='des',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Intended Audience :: Science/Research',
    ]
)
