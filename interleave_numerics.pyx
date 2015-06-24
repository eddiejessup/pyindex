cdef unsigned long part1by3(unsigned long n):
    """
    Inserts three 0 bits between each bit in `n`.

    n: 16-bit integer
    """
    # Zero out all bits above place 16
    n &= 0xFFFF

    n = (n | (n << 27)) & 0o000000777000000000777
    n = (n | (n << 9)) & 0o000770007000000770007
    n = (n | (n << 9)) & 0o700070007000700070007
    n = (n | (n << 3)) & 0o100610061006100610061
    n = (n | (n << 3)) & 0o104210421042104210421

    return n


cdef unsigned long unpart1by3(unsigned long n):
    """
    Gets every fourth bit from `n`.

    n: 32-bit integer
    """
    n &= 0o104210421042104210421

    n = (n | (n >> 3)) & 0o100610061006100610061
    n = (n | (n >> 3)) & 0o700070007000700070007
    n = (n | (n >> 9)) & 0o000770007000000770007
    n = (n | (n >> 9)) & 0o000000777000000000777
    n = (n | (n >> 27)) & 0xFFFF

    return n


def interleave4(unsigned long w, unsigned long x, unsigned long y, unsigned long z):
    """
    Interleaves four numbers in binary representation.

    Uses a method of spacing out the numbers, filled with intermediate zeros,
    then slightly shifting them and combining.

    w, x, y, z: 16-bit integers
    """
    return (part1by3(w) |
            (part1by3(x) << 1) |
            (part1by3(y) << 2) |
            (part1by3(z) << 3))


def deinterleave4(unsigned long n):
    """
    Deinterleaves an integer into four integers.
    """
    return [unpart1by3(n),
            unpart1by3(n >> 1),
            unpart1by3(n >> 2),
            unpart1by3(n >> 3)]
