"""
pow function
y = 100110
x = 10
"""


def power(x: float, y: int) -> float:
    result = 1
    power = y
    if y < 0:
        power = -y
        x = 1/x
    
    while power:
        if power & 1:
            print(bin(power))
            result *= x
        x = x * x
        power = power >> 1
    return result

print(power(2, 7) )