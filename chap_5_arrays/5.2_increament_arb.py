def increament_arb_precision(num):
    num[-1] += 1
    for i in reversed(range(1, len(num))):
        if num[i] != 10:
            break
        num[i - 1] += num[i] // 10
        num[i] %= 10
    if num[0] == 10:
        num[0] = 1
        num.append(0)
        return num
    else:
        return num

num = [9,9,9,9]
print(increament_arb_precision(num))