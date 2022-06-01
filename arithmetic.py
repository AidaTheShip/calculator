## The multicalculator - not just addition, subtraction, division, and multiplication but also complex things 
## such as Matrix multiplication and addition. 
## By Aida Baradari

from distutils.command.build_scripts import first_line_re
from re import T
from tkinter import *
from math import sqrt


# initializing the window
root = Tk()
root.geometry("400x500")
root.resizable(0,0)
root.title("Calculator")

# initializing our entry graphic
e = Entry(root, width = 35, borderwidth = 5)
# inserting the starting value, 0
e.insert(0, 0)
# defining where the entry should be
e.grid(row = 0, column = 0, columnspan=3, padx=10, pady=10)

# defining a number class
class Numbers: 
    # definint the global variable result that will be updated
    global result
    result = 0
    global before
    before = ""
    # defining the instances of buttons
    def __init__(self, idnumber, row, column): 
        self.text = idnumber
        button = Button(root, text = self.text, padx = 40, pady = 20, command = lambda: self.buttonfunction(idnumber), bg = "#000000")
        button.grid(row = row, column = column)
        
    # the function that defines what happens when buttons are pressed
    def buttonfunction(self, entered):
        # the number that was entered
        self.entered = entered
        # getting the current value in the entry so we can construct the total number entered
        currentval = e.get()
        # constructing a value that has more than one digit
        result = int(str(currentval) + str(entered))
        # deleting the old one and inserting the actual real number into the entry
        e.delete(0, END)
        e.insert(0, result)
     
# defining an operator class  
class Operators:
    # defining variables for the other numbers entered
    global fst
    fst = 0
    global snd
    snd = 0
    global result 
    global before
    def __init__(self, operator, row, column, command):
        self.fst = fst
        self.snd = snd 
        self.result = result
        self.before = before    # the operator that was entered before
        self.operator = operator
        self.row = row
        self.column = column 
        self.command = command
        opbutton = Button(root, text = self.operator, padx = 40, pady = 20, command = lambda: command(self))
        opbutton.grid(row = row, column = column)
    # clears what is inside of the entry
    def clear(self):
        e.delete(0, END)
        global result 
        global fst 
        global snd
        global before
        fst = 0 
        snd = 0 
        result = 0 
        before = ""
    def add(self): 
        global before
        global result
        fnum = e.get()
        # clearing the entry after we entered the first number
        e.delete(0, END)
        # we are assigning the value to the result 
        fst = int(fnum)
        if before == "=":
            result = fst
        else: 
            result += fst
        before = "+"
    def subtract(self):
        global before
        global result
        fnum = e.get()
        e.delete(0, END)
        fst = int(fnum)
        result = fst
        before = "-"
    def multiply(self): 
        global before
        global result
        fnum = e.get()
        e.delete(0, END)
        fst = int(fnum)
        result = fst
        before = "*"
    def divide(self):
        global before 
        global result 
        fnum = e.get()
        e.delete(0, END)
        fst = int(fnum)
        result = fst
        before = "/"
    # operation equal, display the result + (operation) 2nd number
    def equal(self):
        global before
        global fst
        global result
        global snd
        # getting the next number we want to do the operation on
        snum = e.get()
        e.delete(0, END) 
        snd = int(snum)
        if before == "+":
            result += snd
        elif before == "-":
            result -= snd
        elif before == "*": 
            result *= snd
        elif before == "/": 
            result = result // snd
        before = "="
        e.insert(0, result)
        

# instantiating the different number blocks we need in a calculator
button9 = Numbers(9, 1, 2)
button8 = Numbers(8, 1, 1)
button7 = Numbers(7, 1, 0)
button6 = Numbers(6, 2, 2)
button5 = Numbers(5, 2, 1)
button4 = Numbers(4, 2, 0)
button3 = Numbers(3, 3, 2)
button2 = Numbers(2, 3, 1)
button1 = Numbers(1, 3, 0)
button0 = Numbers(0, 4, 0)


# instantiating the different binart operators that we want to use
equal = Operators("=", 6, 2, Operators.equal)
add = Operators("+", 4, 1, Operators.add)
subtract = Operators("-", 4, 2, Operators.subtract)
multiplication = Operators("*", 5, 0, Operators.multiply)
division = Operators("/", 5, 1, Operators.divide)
clear = Operators("Clear", 6, 1, Operators.clear)
# to add: division, multiplication, matrices, vectors, calculus, square roots?

# print(fst, snd)
# Operators.add(add)

# Id number will be the number we have to add/subtract/divide/multiplky
# root.mainloop()
while True: 
    print(fst, snd, result)
    root.update() 
    # displaying what you currently entered
    label = Label(root, text = result)
    label.grid(row = 7, column = 0, columnspan = 3)