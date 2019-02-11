"""
idea:
1000100 - parity is 0
1000101 - parity is 1
"""
def calculate_parity(word):
    parity = 0
    while word:
        word = word & (word - 1) # drop the lowest bit
        parity = parity ^ 1
    return parity

PRECOMPUTED_PARITY = []
for i in range(2**16):
    PRECOMPUTED_PARITY.append(calculate_parity(i))

def calculate_parity_long_word(word):
    MASK_SIZE = 16 # bits
    MASK = 0xFFFF
    return (
        PRECOMPUTED_PARITY[word & MASK] ^
        PRECOMPUTED_PARITY[(word >> MASK_SIZE) & MASK] ^
        PRECOMPUTED_PARITY[(word >> MASK_SIZE*2) & MASK] ^
        PRECOMPUTED_PARITY[(word >> MASK_SIZE*3) & MASK]
    )


print(calculate_parity_long_word(0xFFFF0000FFFF003))