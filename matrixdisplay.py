# defining a matrix in the terminal and then doing calculations on it - 2020, uploaded 2022
operationslist = ['multiplication', 'addition', 'printing']

def definingmatrix ():
    # asking for the columns and rows the matrix should have
    i = int(input("columns: "))
    j = int(input("rows: "))
    print(f"We will create a matrix with {i} columns and {j} rows.")
    # matrix in python as form of lists in list
    matrix = [] 
    temp = [] # temporary list storing the elements in a row
    for n1 in range(1, j + 1): 
        for n2 in range(1, i + 1):
            number = int(input(f"Please enter position for row {n1} and column {n2}: "))
            temp.append(number)
        matrix.append(temp)
        temp = []
    return matrix

def operations (): 
    print("These are all the possible things you can do: ")
    for element in operationslist: 
        print("- " + element)
    operation = input("Please input the operation you want to do on a/multiple matrix/matrices: ")
    if operation.lower() == "addition": 
        print("Please enter your two matrices. ")
        addition(definingmatrix(), definingmatrix())
    elif operation.lower() == "multiplication": 
        print("Please enter your two matrices. ")
        multiplication(definingmatrix(), definingmatrix()) 
    elif operation.lower() == "printing": 
        print("Please enter the matrix. ")
        printing (definingmatrix())

def addition (matrix1, matrix2): 
    print(matrix1 + matrix2)
     
def multiplication (A, B):
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
    printing(returnmatrix)

# printing the matrix to terminal
def printing(matrix):
    for row in matrix: 
        print(row)

# a different way of displaying the matrix, if you don't want the elements in a list
def printmatrixnotaslist(matrix): 
    print("\n")
    for row in matrix:
        for element in row:
            print(element, end = " ")
        print("\n")
operations()