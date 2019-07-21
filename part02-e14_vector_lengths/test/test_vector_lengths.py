#!/usr/bin/env python3

import unittest
from unittest.mock import patch

import numpy as np
import scipy.linalg

from tmc import points

from tmc.utils import load, get_out

module_name="src.vector_lengths"
vector_lengths = load(module_name, "vector_lengths")
main = load(module_name, "main")

def patch_name(m, d):
    import importlib
    parts=d.split(".")
    try:
        getattr(importlib.import_module(m), parts[-1])
        p=".".join([m, parts[-1]])
    except ModuleNotFoundError:
        raise
    except AttributeError:
        if len(parts) == 1:
            raise
        try:
            getattr(importlib.import_module(m), parts[-2])
            p=".".join([m] + parts[-2:])
        except AttributeError:
            if len(parts) == 2:
                raise
            getattr(importlib.import_module(m), parts[-3])
            p=".".join([m] + parts[-3:])
    return p

@points('p02-14.1')
class VectorLengths(unittest.TestCase):


    def test_content(self):
        n=10
        for m in range(1,5):
            a=np.random.randn(n, m)
            v=vector_lengths(a)
            self.assertEqual(v.shape, (n,), msg="Incorrect shape!")
            correct=scipy.linalg.norm(a, 2, axis=1)
            np.testing.assert_allclose(v, correct,
                                       err_msg="Incorrect result for matrix:\n%s" % a)

    def test_calls(self):
        a=np.random.randn(10,3)
        with patch(patch_name(module_name, "np.sum"), wraps=np.sum) as psum:
            with patch(patch_name(module_name, "np.sqrt"), wraps=np.sqrt) as psqrt:
                v=vector_lengths(a)
                psum.assert_called_once()
                psqrt.assert_called_once()

    def test_main(self):
        with patch(patch_name(module_name, "vector_lengths"), wraps=vector_lengths) as vl:
            main()
        self.assertGreaterEqual(vl.call_count, 1,
                                msg="You should call the vector_lengths function from the main function!")

    def test_no_scipy(self):
        a=np.random.randn(10,3)
        try:
            with patch(patch_name(module_name, "scipy.linalg.norm")) as pnorm:
                v=vector_lengths(a)
                pnorm.assert_not_called()
        except AttributeError:
            pass

if __name__ == '__main__':
    unittest.main()

