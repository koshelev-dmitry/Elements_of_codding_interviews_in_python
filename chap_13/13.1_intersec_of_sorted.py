def intersection_of_sorted_arrays(A, B):
    a = 0 
    b = 0
    intersection = []
    while a < len(A) and b < len(B):
        if A[a] == B[b]:
            if intersection == [] or intersection[-1] != A[a]:
                intersection.append(A[a])
            a += 1
            b += 1
        elif A[a] > B[b]:
            b += 1
        elif A[a] < B[b]:
            a += 1
    return intersection

A = [1,2,3,4,4, 5,6]
B = [4]
inters = intersection_of_sorted_arrays(A, B)
print(inters)