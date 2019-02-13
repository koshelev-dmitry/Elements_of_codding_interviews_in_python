def compute_alternation(A):
    # [1,2,6,4,3,2,5,6,7]
    for i in range(len(A)-1):
        if i % 2 == 1:
            if A[i] < A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
        else:
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
    
A = [1,2,6,4,3,2,5,6,7]
print(A)
compute_alternation(A)
print(A)