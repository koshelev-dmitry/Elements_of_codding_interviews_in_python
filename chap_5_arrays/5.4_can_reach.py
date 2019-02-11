def can_reach_end(A):
    furthest_reached = 0
    last_index = len(A)-1
    i = 0
    while i <= furthest_reached and furthest_reached < last_index:
        furthest_reached = max(furthest_reached, i + A[i])
        i += 1
    return furthest_reached >= last_index 

print(can_reach_end([3,0,0]))