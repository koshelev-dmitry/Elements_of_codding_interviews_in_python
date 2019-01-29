def fibonacci(n):
    if n<=1:
        return n
    f_min_2 = 0
    f_min_1 = 1
    for _ in range(1, n):
        f = f_min_2 + f_min_1
        f_min_2, f_min_1 = f_min_1, f
    return f
    
    
