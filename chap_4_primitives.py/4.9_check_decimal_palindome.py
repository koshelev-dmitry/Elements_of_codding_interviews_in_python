"""
not palindrom if a number is negative
not palindrom if it ends with 0
"""

def is_palindrom(x):
    if x <= 0:
        return x == 0
    import math
    num_of_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10 ** (num_of_digits - 1)

    for _ in range(num_of_digits // 2):
        if x // msd_mask != x % 10:
            return False
        x = x % msd_mask # remove msd
        x = x // 10 # remove lsd
        msd_mask //= 100
    return True


print(is_palindrom(-111))