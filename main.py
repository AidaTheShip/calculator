from tkinter import *

from numpy import matrix

root = Tk()
root.title("Choose Calculation option")
root.geometry("300x300")

label= Label(root, text = "Please choose the operation.").pack() 

# defining the launch function, calling the code when a specfic option is chosen
def launch(): 
    if choice.get() == "Arithmetic":
        import arithmetic
        arithmetic.call("main.py", shell = True)
    elif choice.get() == "Matrixmultiplication":
        import matrixmulitplicationfile as mat
        mat.call("main.py", shell = True)
    elif choice.get() == "Calculus": 
        pass


# options that the calculator can do
options = ["Arithmetic", "Matrixmultiplication", "Calculus"]

choice = StringVar() 
choice.set(options[0])

# defining the dropdown menu 
dropdown = OptionMenu(root, choice, *options).pack()

launchbutton = Button(root, text = "Launch", command = launch, padx = 50, pady = 100).pack()

root.mainloop()
