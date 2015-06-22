#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `interleave`"""

import unittest
import interleave


class TestInterleave(unittest.TestCase):

    def test_interleave2(self):
        self.assertEqual(hex(interleave.interleave2(0x00, 0xFF)),
                         '0xaaaa')
        self.assertEqual(bin(interleave.interleave2(0b00000000, 0b11111111)),
                         '0b1010101010101010')
        self.assertEqual(hex(interleave.interleave2(0x0000, 0xFFFF)),
                         '0xaaaaaaaa')

    def test_interleave3(self):
        self.assertEqual(hex(interleave.interleave3(0x00, 0xFF, 0x00)),
                         '0x492492')
        self.assertEqual(hex(interleave.interleave3(0x0000, 0xFFFF, 0x0000)),
                         '0x12492492')

    def test_interleave4(self):
        self.assertEqual(hex(interleave.interleave4(0x00, 0xFF, 0x00, 0x00)),
                         '0x44444444')


if __name__ == '__main__':
    unittest.main()
