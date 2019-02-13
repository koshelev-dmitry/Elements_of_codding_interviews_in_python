def max_profit(A):
    # create two arrays
    # one in forward move: starting from first dat, ->
    # one in backward move: starting from last day, going backward <-

    min_val = A[0]
    max_profit = 0
    forward_profit = [0]*len(A)
    for i in range(len(A)):
        min_val = min(min_val, A[i])
        max_profit = max(max_profit, A[i]-min_val)
        forward_profit[i] = max_profit

    max_val = A[-1]
    max_profit = 0
    backward_profit = [0]*len(A)
    for i in reversed(range(len(A))):
        max_val = max(max_val, A[i])
        max_profit = max(max_profit, max_val - A[i])
        backward_profit[i] = max_profit  

    print(forward_profit)
    print(backward_profit)

    total_profit = 0
    for i in range(0, len(backward_profit)):
        if i == 0:
            total_profit = max(total_profit, backward_profit[i])
        else:
            total_profit = max(total_profit, backward_profit[i] + forward_profit[i-1])
    return total_profit

A = [12,11,13,9,12,8,14,13,15]
print(max_profit(A))