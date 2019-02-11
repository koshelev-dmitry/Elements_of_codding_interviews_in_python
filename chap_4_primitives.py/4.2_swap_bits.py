"""
00110001001
swap bits at i and j
idea:
1) do we need to swap bits?
2) if yes swap
"""

def swap_bits(word, i, j):
    # ckeck if we need swap
    if (word>>i) & 1 != (word>>j) & 1:
        return word ^ ( (1<<i) | (1<<j))
    return word

assert swap_bits(3, 3, 1) ==  9 # 0b0011=3 => 0b1001=9
assert swap_bits(3, 3, 0) ==  10 # 0b0011=3 => 0b1010=9

