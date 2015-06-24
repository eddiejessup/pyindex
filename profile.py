#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division
import timeit
import numpy as np
import interleave
import interleave_numerics

num_sets = []
num_sets.append(4 * [2 ** 16 - 1])
num_sets.append(4 * [0])
num_sets.extend(np.random.randint(0, 2 ** 16 - 1, (1000, 4)))


def interleave4_str():
    for nums in num_sets:
        interleave.interleavem(*nums)


def interleave4_naive():
    for nums in num_sets:
        interleave.interleavem_naive(*nums)


def interleave4_cheat():
    for nums in num_sets:
        interleave.interleave4_cheat(*nums),


def interleave4():
    for nums in num_sets:
        interleave.interleave4(*nums),


def interleave4_cython():
    for nums in num_sets:
        interleave_numerics.interleave4(*nums)


def main():
    print('Naïve: ',
          timeit.timeit('interleave4_naive()',
                        setup="from __main__ import interleave4_naive",
                        number=100))
    print('Parting using strings: ',
          timeit.timeit('interleave4_str()',
                        setup="from __main__ import interleave4_str",
                        number=100))
    print('Parting using two-step bit shifting: ',
          timeit.timeit('interleave4_cheat()',
                        setup="from __main__ import interleave4_cheat",
                        number=100))
    print('Parting using one-step bit shifting: ',
          timeit.timeit('interleave4()',
                        setup="from __main__ import interleave4",
                        number=100))
    print('Parting using one-step bit shifting cython: ',
          timeit.timeit('interleave4_cython()',
                        setup="from __main__ import interleave4_cython",
                        number=100))

if __name__ == '__main__':
    main()
