def sample_online_data(data, k):
    import random
    sampling_result = list(data[:k])
    num_seen_so_far = k
    for x in data:
        num_seen_so_far += 1
        ind_to_replace = random.randrange(num_seen_so_far)
        if ind_to_replace < k:
            sampling_result[ind_to_replace] = x
    return sampling_result