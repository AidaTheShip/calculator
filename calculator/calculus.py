from curses import raw
from tkinter import * 
from PIL import ImageTk, Image
import numpy as np 
import sympy as sp
import re

root = Tk()
root.geometry("600x600")
root.title("Calculus")

global resulting
resulting = 0
# integrate(f, x) returns the indefinite integral 
# integrate(f, (x, a, b)) returns the definite integral 

# defining the variable we will use for integration
x = sp.Symbol("x")
global i
i = 8
# function that transforms entry into actual function expression
def calc(): 
    # getting the entries for the lower and upperbound and the function
    upper = upperbound.get()
    lower = lowerbound.get()
    f = functionentry.get()
    global resulting
    resulting = "                                                                                                      "
    if upper == "" and  lower == "":
        return sp.integrate(f, x)
    elif upper == "" and lower != "" or lower == "" and upper != "": 
        return "Please check your bounds and enter again."
    else: 
        return sp.integrate(f, (x, lower, upper))

def clicked():
    global i
    global resulting
    resulting = calc()
    
    result = Label(root, text = resulting)
    result.config(font=('Helvetica bold',40))
    result.grid(row = i, column = 0, columnspan=10)
    i += 10
        

explanation = """\nEnter the function you want to take an integral of.
            If you want the indefinite integral leave the bounds blank.
            Add all arithmetic symbols, and parantheses around functions (cos(x), sin(x), etc.) \n"""

# initiating the interface
explanation = Label(root, text = explanation)
explanation.grid(row = 0, column = 0, columnspan = 10, rowspan = 3)

functionlabel = Label(root, text = "Enter f(x):")
functionlabel.grid(row = 4, column = 0)
functionentry = Entry(root, width = 5, borderwidth = 3)
functionentry.grid(row = 4, column = 1)

upperboundlabel = Label(root, text = "Upperbound b:")
upperboundlabel.grid(row = 6, column = 0)
upperbound = Entry(root, width = 5, borderwidth = 3)
upperbound.grid(row = 6, column =1)

lowerboundlabel = Label(root, text = "Lowerbound a: ")
lowerboundlabel.grid(row = 5, column = 0)
lowerbound = Entry(root, width = 5, borderwidth = 3)
lowerbound.grid(row = 5, column = 1)

calculatebutton = Button(root, text = "Calculate", padx = 20, pady =20, command = clicked)
calculatebutton.grid(row = 7, column = 1)


 

while True: 
    root.update()
    