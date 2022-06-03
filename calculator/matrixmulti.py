# matrix multiplication algorithm in Python, there is probably an easier way but it's okay. 
# by Aida Baradari 23.05.2022
from numpy import array


# A = [[1,2],[3,4]]
# B = [[2,0],[2,0]]
def multiplication(A, B):
    returnmatrix = []
    i = 0
    j = 0
    k = 0
    rowmatrix = []
    # product of one cell
    product = 0
    # while i is smaller than the number of rows in the matrix
    while i < len(A):
        # j is smaller than the number of columns in the matrix we multiply by
        while k < len(B[0]): 
            while j < len(B):
               product += A[i][j] * B[j][k]
               j += 1
            rowmatrix.append(product)
            product = 0
            j = 0
            k += 1
        returnmatrix.append(rowmatrix)
        rowmatrix = []
        i += 1
        k = 0 
    print(returnmatrix)
    return returnmatrix

