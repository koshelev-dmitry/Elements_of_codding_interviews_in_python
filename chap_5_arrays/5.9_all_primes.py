def enumerate_all_primes(n):
    result = []
    candidates = [False, False] + [True] * (n-1)
    for i in range(2, n):
        if candidates[i] == True:
            result.append(i)
            # mark all candidates i*N as False
            for j in range(i, n, i):
                candidates[j] = False
    return result

print(enumerate_all_primes(100))
