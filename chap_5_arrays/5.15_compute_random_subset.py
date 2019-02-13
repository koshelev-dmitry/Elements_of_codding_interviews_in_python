def compute_random_subset(n,k):
    # return size-k subset of [0,1,2,3,...,n-1]
    import random 
    changed_element = {}
    for i in range(k):
        # generate a random index between i and n-1
        rand_indx = random.randrange(i, n)
        rand_indx_mapped = changed_element.get(rand_indx, rand_indx)
        i_mapped = changed_element.get(i, i)
        changed_element[rand_indx] = i_mapped
        changed_element[i] = rand_indx_mapped
    return [changed_element[i] for i in range(k)]


print(compute_random_subset(5,2))