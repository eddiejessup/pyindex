#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `interleave`"""

from __future__ import print_function, division
import unittest
import numpy as np
import interleave
import interleave_numerics


class TestInterleave(unittest.TestCase):
    num_sets = []
    num_sets.append(5 * [2 ** 16 - 1])
    num_sets.append(5 * [0])
    num_sets.extend(np.random.randint(0, 2 ** 16 - 1, (1000, 5)))

    def test_interleavem(self):
        for nums in self.num_sets:
            n_nums = np.random.randint(2, 6)
            self.assertEqual(interleave.interleavem_naive(*nums[:n_nums]),
                             interleave.interleavem(*nums[:n_nums]))

    def test_interleave2(self):
        for nums in self.num_sets:
            self.assertEqual(interleave.interleave2(*nums[:2]),
                             interleave.interleavem_naive(*nums[:2]))

    def test_interleave3(self):
        for nums in self.num_sets:
            self.assertEqual(interleave.interleave3(*nums[:3]),
                             interleave.interleavem_naive(*nums[:3]))

    def test_interleave4(self):
        for nums in self.num_sets:
            self.assertEqual(interleave.interleave4(*nums[:4]),
                             interleave.interleavem_naive(*nums[:4]))

    def test_interleave4_cython(self):
        for nums in self.num_sets:
            self.assertEqual(interleave_numerics.interleave4(*nums[:4]),
                             interleave.interleavem_naive(*nums[:4]))

    def test_interleave4_cheat(self):
        for nums in self.num_sets:
            self.assertEqual(interleave.interleave4_cheat(*nums[:4]),
                             interleave.interleavem_naive(*nums[:4]))

    def test_interleave5(self):
        for nums in self.num_sets:
            self.assertEqual(interleave.interleave5(*nums),
                             interleave.interleavem_naive(*nums))

    def test_idempotency2(self):
        for nums in self.num_sets:
            integers = list(nums[:2])
            interleaved = interleave.interleave2(*integers)
            self.assertEqual(integers, interleave.deinterleave2(interleaved))

    def test_idempotency3(self):
        for nums in self.num_sets:
            integers = list(nums[:3])
            interleaved = interleave.interleave3(*integers)
            self.assertEqual(integers, interleave.deinterleave3(interleaved))

    def test_idempotency4(self):
        for nums in self.num_sets:
            integers = list(nums[:4])
            interleaved = interleave.interleave4(*integers)
            self.assertEqual(integers, interleave.deinterleave4(interleaved))

    def test_idempotency4_cython(self):
        for nums in self.num_sets:
            integers = list(nums[:4])
            interleaved = interleave_numerics.interleave4(*integers)
            self.assertEqual(integers,
                             interleave_numerics.deinterleave4(interleaved))

    def test_idempotency5(self):
        for nums in self.num_sets:
            integers = list(nums[:5])
            interleaved = interleave.interleave5(*integers)
            self.assertEqual(integers, interleave.deinterleave5(interleaved))

    def test_idempotencym(self):
        for nums in self.num_sets:
            n_nums = np.random.randint(2, 6)
            integers = list(nums[:n_nums])
            interleaved = interleave.interleavem(*integers)
            self.assertEqual(integers, interleave.deinterleavem(interleaved,
                                                                n_nums))


if __name__ == '__main__':
    unittest.main()
