def dutch_flag_partitioning(A, i):
    pivot = A[i]

    hi = len(A) - 1 
    lo = 0
    curr = 0
    while curr <= hi:
        print(A)
        if A[curr] == pivot:
            curr += 1
        elif A[curr] < pivot:
            A[curr], A[lo] = A[lo], A[curr]
            lo += 1
            curr += 1
        else: # A[curr] > pivot:
            A[curr], A[hi] = A[hi], A[curr]
            hi -= 1
    print(A)    

dutch_flag_partitioning([2,0,5,1,2,0,1,3], 0)
