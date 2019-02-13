def delete_duplicates(A):
    insertion_curr = 1
    for i in range(1,len(A)):
        if A[i] != A[i-1]:
            A[insertion_curr] = A[i]
            insertion_curr += 1
    return insertion_curr


A = [2,2,2,2,3,3,3,3,5,5,7,11,11,11,13]
print(delete_duplicates(A))
print(A)