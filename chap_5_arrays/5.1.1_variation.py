def sort_four_elements(A):
    abcd = set(A)
    a = min(abcd)
    abcd.remove(a)
    b = min(abcd)
    abcd.remove(b)
    c = min(abcd)
    d = max(abcd)
    def swap(i, j):
        A[i], A[j] = A[j], A[i]

    i_a, i_b, i_c, i_d = 0, 0, len(A)-1, len(A)-1
    while i_b <= i_c:
        print(A)
        if A[i_b] == c:
            swap(i_b, i_c)
            i_c -= 1
        elif A[i_b] == d:
            swap(i_b, i_d)
            i_d -= 1
        elif A[i_b] == b:
            i_b += 1
        else:  # A[i_b] == a
            swap(i_b, i_a)
            i_a += 1
            i_b += 1
    print('result', A)


sort_four_elements([1,2,3,4,1,2,3,4,1,2,3,4,3,4,1,2])
