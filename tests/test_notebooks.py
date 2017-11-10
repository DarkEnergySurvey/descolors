#!/usr/bin/env python
"""
Test ipython notebooks in skymap tutorial.

Adapted from:
https://blog.thedataincubator.com/2016/06/testing-jupyter-notebooks/
"""
__author__ = "Alex Drlica-Wagner"

import os
import unittest
import glob

import subprocess
import tempfile

import nbformat

def _notebook_run(path):
    """Execute a notebook via nbconvert and collect output.
       :returns (parsed nb object, execution errors)
    """
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
          "--ExecutePreprocessor.timeout=60",
          "--output", fout.name, path]
        subprocess.check_call(args)

        fout.seek(0)
        nb = nbformat.read(fout, nbformat.current_nbformat)

    errors = [output for cell in nb.cells if "outputs" in cell
                     for output in cell["outputs"]\
                     if output.output_type == "error"]

    return nb, errors


class TestNotebooks(unittest.TestCase):
    """ Test the tutorial ipython notebooks. """

    def _test_notebook(self, name=''):
        """ Test a specific chapter of the tutorial. """
        path = glob.glob('examples/%s'%name)[0]
        abspath = os.path.abspath(path)
        nb, errors = _notebook_run(abspath)
        assert errors == []

    def test_colors(self):
        return self._test_notebook('des_colors.ipynb')



if __name__ == "__main__":
    unittest.main()
