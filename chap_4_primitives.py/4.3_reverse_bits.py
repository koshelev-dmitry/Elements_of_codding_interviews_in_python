"""
100011 -> 110001
idea:
take the last bit from entrance and push it to the result
"""

def reverse_bits(word):
    result = 0
    while word:
        get_bit = word & 1
        word = word >> 1 # push word
        result = (result << 1) # whift result by one
        result = result ^ get_bit
    return result


for i in range(0, 1000, 200):
    word = i
    print(i, '=', bin(word))

    reverse = reverse_bits(word)
    print(bin(reverse))