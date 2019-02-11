"""
Find the closest integer with the same weight
92 = 0b1011100, wight = 4
idea:
find smallest bits that are 01 or 10 and swap them
"""

def find_closest(word):
    x = word
    i = 0
    while (x >> 1) & 1 == x & 1:
        i += 1
        x = x >> 1
    mask = 0b11 << i
    return word ^ mask

print(find_closest(6))