def advancing_through_array(A):
    """
    Idea:
    0) Iterate through each element in A
    1) record how far we can go from each position
    2) keep the maximum we can go
    3) if the current position is not reacheble return False
    """
    max_reacheable_index = A[0]
    for i in range(len(A)):
        if max_reacheable_index < i:
            return False
        max_reacheable_index = max(i + A[i], max_reacheable_index)
        if max_reacheable_index >= len(A)-1:
            return True

A = [3,2,0,1,2,0,1]
print(advancing_through_array(A))