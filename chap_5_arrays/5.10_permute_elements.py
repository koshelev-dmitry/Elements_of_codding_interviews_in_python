"""
{a,b,c,d}
Permutation P:
P[i] is the location of the element at i after permutation
{a,b,c,d} = array
{2,0,1,3} = Permutation
{b,c,a,d} = permutaion is applied
"""
def apply_permutation(A, P):
    for i in range(len(A)):
        while P[i] != i:
            index_1 = i
            index_2 = P[i]
            A[index_1], A[index_2] = A[index_2], A[index_1]
            P[index_1], P[index_2] = P[index_2], P[index_1]

A = ['a','b','c','d','e','f','g']
P = [ 2,  3,  1,  5,  0,  4,  6]
apply_permutation(A, P)
print(A)
