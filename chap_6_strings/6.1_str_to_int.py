def string_to_integer(str_int):
    sign = 1
    result = 0
    for c in str_int:
        if c != '-':
            result = result*10 + ord(c) - ord('0')
        else:
            sign = -1
    return result*sign

def int_to_string(num):
    result = []
    is_negative = False
    if num < 0:
        num = -num
        is_negative = True

    while num:
        result.append(chr(num % 10 + ord('0')))
        num //= 10

    if is_negative:
        result.append('-')
    return ''.join(reversed(result))


if __name__ == "__main__":
    import pprint as pp
    pp.pprint(string_to_integer('-1234') + 1)
    pp.pprint(int_to_string(-2134))