"""
<2,0,1> < <2,1,0>
"""

def next_permutation(perm):
    # perm = <2,3,4,1,0>
    # find from the end find the longest increasing sequence
    curr = len(perm) - 2
    while curr >= 0 and perm[curr] > perm[curr+1]:
        curr -= 1
    if curr == -1:
        return []

    # find element to swap
    i = len(perm) - 1
    while perm[i] < perm[curr]:
        i -= 1

    # swap
    perm[curr], perm[i] = perm[i], perm[curr]

    # reverse
    perm[curr+1:] = reversed(perm[curr+1:])
    return perm 


perm = [0,1,2,3]
print(next_permutation(perm))
print(next_permutation(perm))
print(next_permutation(perm))
print(next_permutation(perm))
print(next_permutation(perm))
print(next_permutation(perm))


