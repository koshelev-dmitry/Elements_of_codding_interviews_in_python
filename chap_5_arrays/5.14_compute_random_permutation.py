def sample_offline_data(data, k):
    import random
    for i in range(k):
        r = random.randint(i, len(data)-1)
        data[r], data[i] = data[i], data[r]


def compute_random_permutation(n):
    permutation = list(range(n))
    sample_offline_data(permutation, n)
    return permutation

print(compute_random_permutation(10))