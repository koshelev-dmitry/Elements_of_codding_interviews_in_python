def multiply_two_nums(num1, num2):
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])
    result = [0]*(len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i+j+1] += num1[i] * num2[j]
            result[i+j] += result[i+j+1] // 10
            result[i+j+1] %= 10
    i = 0
    while result[i] == 0:
        i += 1
    
    result[i] *= sign
    return result[i:]

num1 = [-1,1,1]
num2 = [1,1,1]
print(multiply_two_nums(num1, num2))

