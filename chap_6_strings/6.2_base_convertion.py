def base_convertion(numeric, b1, b2):
    # convert to 10
    HEX = {10: 'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    
    base10 = 0
    for i, c in enumerate(reversed(numeric)):
        base10 += (ord(c) - ord('0')) * b1**i

    # convert to base b2
    base_b2 = []
    while base10:
        candidate = base10 % b2
        if candidate in HEX:
            base_b2.append(HEX[candidate])
        else:
            base_b2.append(chr(candidate + ord('0')))

        base10 = base10 // b2
    return ''.join(reversed(base_b2))


if __name__ == "__main__":
    x = base_convertion('615', 7, 13)
    print(x)