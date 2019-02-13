def partition_dutch_flag(A, i):
    pivot = A[i]
    l = 0
    r = len(A)-1
    curr = 0
    while curr < r:
        if A[curr] < pivot:
            A[l], A[curr] = A[curr], A[l]
            l += 1
            curr += 1
        elif A[curr] > pivot:
            A[r], A[curr] = A[curr], A[r]
            r -= 1
        else:
            curr += 1

A = [1,9,3,4,5,1,4,0,6,1]
print(A)
partition_dutch_flag(A, 0)
print(A)
