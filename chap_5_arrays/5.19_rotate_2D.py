def rotate_2D(A):
    n = len(A) - 1
    
    for i in range(len(A) // 2):
        for j in range(i, n - i):
            # swap
            (A[i][j],  # (0,0) = 1
            A[~j][i], # (-1,0) = 13
            A[~i][~j], #(-1,-1) = 16
            A[j][~i]) =(A[~j][i], # (-1, 0) = 13
                        A[~i][~j],
                        A[j][~i], 
                        A[i][j])  


A = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]
rotate_2D(A)
print(A)