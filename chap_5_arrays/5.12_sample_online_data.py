def sample_offline_data(data, k):
    import random
    for i in range(k):
        r = random.randint(i, len(data)-1)
        data[r], data[i] = data[i], data[r]
