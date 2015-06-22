# -*- coding: utf-8 -*-

from __future__ import print_function, division
from math import ceil


def pad_with_zeros(s, n):
    return '0' * (n - len(s)) + s


def pad_bin(b, n):
    return pad_with_zeros(bin(b)[2:], n)


def part1by1(n):
    """
    Inserts one 0 bit between each bit in `n`.

    n: 16-bit integer
    """
    n &= 0x0000FFFF

    n = (n | (n << 8)) & 0x00FF00FF
    n = (n | (n << 4)) & 0x0F0F0F0F
    n = (n | (n << 2)) & 0x33333333
    n = (n | (n << 1)) & 0x55555555

    return n


def part1by2(n):
    """
    Inserts two 0 bits between each bit in `n`.

    n: 16-bit integer
    """
    n &= 0x000003FFF

    n = (n ^ (n << 16)) & 0xFF0000FF
    n = (n ^ (n << 8)) & 0x0300F00F
    n = (n ^ (n << 4)) & 0x030C30C3
    n = (n ^ (n << 2)) & 0x09249249

    return n


def part1by3(n):
    s = bin(n)[2:]
    p = ''
    for e in s:
        p += e + '000'
    return int('0b' + p[:-2:], base=2)


def interleave2(x, y):
    max_bits = max(x.bit_length(), y.bit_length())
    iterations = int(ceil(max_bits / 16))

    ret = 0
    for i in range(iterations):
        interleaved = part1by1(x & 0xFFFF) | (part1by1(y & 0xFFFF) << 1)
        ret |= interleaved << (32 * i)

        x = x >> 16
        y = y >> 16
    return ret


def interleave3(x, y, z):
    return part1by2(x) | (part1by2(y) << 1) | (part1by2(z) << 2)


def interleave4(w, x, y, z):
    return (part1by3(w) |
            (part1by3(x) << 1) |
            (part1by3(y) << 2) |
            (part1by3(z) << 3))
