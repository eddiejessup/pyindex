# Notes on Interleave solution, Elliot Marsden, 2015/06/24

- It seemed like the `part1by2` function didn't work for integers with more than 14 bits, so I changed it slightly.
- In finding the correct shifts and masks to apply for `part1by3`, I accidentally made an `interleave5` function, so I thought I'd leave it in.
- For ease of testing, I made the naive solution work for an arbitrary list of integers, so that's what the `interleavem_naive` function is.
- As the next attempt at optimisation I made the arbitrary list function do the zero-padding method, so that's what the `part1bym`, `interleavem` functions are. Turns out that was slower.
- I then did a specific `interleave4_cheat` function, which does actual bit shifting rather than string manipulation, but parts the integers by applying `part1by1` twice, which is a bit slow.
- So then I wrote `interleave4`, which does the bit shifting properly, in one step.
- Then since you mentioned it, I implemented the `interleave4` in Cython, which is quite a bit faster.
- I've then written deinterleave functions which follow the same pattern (arbitrary-length list functions, then ones for specific numbers of integers, and a Cython implementation).
- The Cython extension can be compiled using `python setup.py build_ext --inplace`. There's also `profile.py` that shows the time to run each version.
