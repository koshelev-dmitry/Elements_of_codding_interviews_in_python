def reverse_digits(x):
    revers = 0
    x_remaning = abs(x)

    while x_remaning:
        revers = revers * 10 + x_remaning % 10
        x_remaning //= 10
    return -revers if x < 0 else revers


print(reverse_digits(1232))