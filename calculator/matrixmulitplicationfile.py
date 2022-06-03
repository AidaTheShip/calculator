from tkinter import * 
import matrixmulti as mat
root = Tk()
root.title("Matrixmultiplication")

global rows
global columns
global x2
global y2
rows = 0
columns = 0
x2 = 2
y2 = 1

# # Creating the input field for the matrix
row = Entry(root, width = 5, borderwidth = 2)
row.grid(row = 0, column = 1)
row.insert(0, rows)
rowlabel = Label(root, text = "Columns: ")
rowlabel.grid(row = 0, column = 0)


column = Entry(root, width = 5, borderwidth = 2)
column.grid(row = 0 , column = 3)
columnlabel = Label(root, text = "Rows: ")
columnlabel.grid(row = 0, column = 2)
column.insert(0,columns)

# Entrys and StringVars
text_var1 = []
entries1 = []

text_var2 = []
entries2 = []
A = []
B = []

# callback function to get the StringVars
def get_matrix(matrix1, matrix2, rows1, columns1, rows2, columns2, var1, var2): 
    matrix1, matrix2 = [],[]
    for i1 in range(rows1): 
        matrix1.append([])
        for j1 in range(columns1): 
            matrix1[i1].append(int(var1[i1][j1].get()))
    for i2 in range(rows2): 
        matrix2.append([])
        for j2 in range(columns2): 
            matrix2[i2].append(int(var2[i2][j2].get()))
    global result
    result = mat.multiplication(matrix1, matrix2)
    resulttext = formatmatrix(result)
    print(resulttext)
    resultlabel = Label(root,text = resulttext).place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)
    
def formatmatrix(matrix):
    output = ""
    for row in matrix:
        for element in row: 
            output += str(element) + "    "
        output += "\n\n"
    return output

# CREATING THE MATRIX
class Matrix:
    def __init__(self, rows, columns, x2, y2, entry, variable):
        self.rows = rows
        self.columns = columns
        self.x2 = x2
        self.y2 = y2
        self.entry = entry
        self.variable = variable
        for i in range(rows):
            variable.append([])
            entry.append([])
            for j in range(columns):
                variable[i].append(StringVar())
                entry[i].append(Entry(root, textvariable = variable[i][j], width = 3))
                entry[i][j].grid(row=x2, column=y2)
                x2 += 1
            
            y2 +=1
            x2 = self.x2
def setting(): 
    global rows1
    global columns1
    rows1 = int(row.get())
    columns1 = int(column.get())
    fstmatrix = Matrix(rows1, columns1, 2, 1, entries1, text_var1)
    global x2
    global y2
    mathematicalcross = Label(root, text="x").grid(row = 2 + rows1, column = 1 + columns1)

def setting2():
    global rows2
    global columns2
    rows2 = int(row.get())
    columns2 = int(column.get())
    second = Matrix(rows2, columns2, 3 + rows2, 1, entries2, text_var2)
    
button = Button(root, text = "Set first Matrix", command = setting).grid(row = 0, column = 5)
button2 = Button(root, text = "Set second Matrix", command = setting2).grid(row = 0, column = 6)
getin = Button(root, text = "Calculate the product.", command = lambda:get_matrix(A, B, rows1, columns1, rows2, columns2, text_var1, text_var2)).grid(row = 0, column = 7)


root.mainloop()
