def non_uniform(nums, probs):
    from random import random
    from bisect import bisect
    from itertools import accumulate
    probs_accumulated = list(accumulate(probs))
    interval = bisect(probs_accumulated, random())
    return nums[interval]

for _ in range(10):
    print(non_uniform([1,2,3,4,5], [0.1, 0.2, 0.3, 0.4, 0.5]))