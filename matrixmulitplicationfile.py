from tkinter import * 
root = Tk()
root.title("Matrixmultiplication")
root.geometry("400x500")

global rows
global columns
rows = 3
columns = 3

# # Creating the input field for the matrix
row = Entry(root, width = 5, borderwidth = 2)
row.grid(row = 0, column = 1)
row.insert(0, rows)
rowlabel = Label(root, text = "Rows: ")
rowlabel.grid(row = 0, column = 0)


column = Entry(root, width = 5, borderwidth = 2)
column.grid(row = 0 , column = 3)
columnlabel = Label(root, text = "Columns: ")
columnlabel.grid(row = 0, column = 2)
column.insert(0,columns)

# Entrys and StringVars
text_var = []
entries = []

# callback function to get the StringVars
def get_matrix(): 
    global rows
    global columns
    matrix = []
    for i in range(rows): 
        matrix.append([])
        for j in range(columns): 
            matrix[i].append(text_var[i][j].get())
    print(matrix)
global x2
global y2
x2 = 2
y2 = 1

# CREATING THE MATRIX
class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        global x2
        global y2
        for i in range(rows):
            text_var.append([])
            entries.append([])
            for j in range(columns):
                text_var[i].append(StringVar())
                entries[i].append(Entry(root, textvariable = text_var[i][j], width = 3))
                entries[i][j].grid(row=x2, column=y2)
                x2 += 1
            
            y2 +=1
            x2 = 2
    def __delete__(self): 
        
def setting(): 
    global rows
    global columns
    rows = int(row.get())
    columns = int(column.get())
    del beginningmatrix

Matrix(rows, columns)

button = Button(root, text = "click me", command = setting).grid(row = 0, column = 5)
# def initiate():
#     global rows
#     global columns
#     nrow = row.get() 
#     ncolumn = row.get()
# # the number of rows and columns based on what you enter!!
#     rows = int(nrow)
#     columns = int(ncolumn)
#     print(rows, columns)
#     matrix2 = Matrix(rows, columns)
#     print(matrix2)
# button = Button(root, text = "click", command = get_matrix).place(x=200, y = 100)
while True: 
    print(rows, columns)
    root.update()
