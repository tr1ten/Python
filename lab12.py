from tkinter import *
from tkinter.ttk import *


# experiment 1

def exp1():
    root1 = Tk()
    root1.title("First_Program")
    root1.mainloop()

# exp1()



# experiment 2
 

def exp2():
    root = Tk()
    root.title("Second_program")
    label = Label(root, text ="Hello World !").pack()
    root.mainloop()

# exp2()



# experiment 3
 

def exp3():
    root = Tk()
    root.title("Second_program")
    label = Label(root, text ="Hello World !" , font=("Arial", 25)).pack()
    root.mainloop()

# exp3()



# experiment 4

def exp4():
    root1 = Tk()
    root1.title("Variable Size Window")
    root1.geometry("700x700")
    root1.mainloop()

# exp4()

# experiment 5

def exp5():
    root1 = Tk()
    root1.title("Fixed Size Window")
    root1.geometry("700x700")
    root1.resizable(False  , False)
    root1.mainloop()

exp5()

# def tupleSort():
#     x = [(4, 1), (1, 2), (6, 0)]
#     x  = sorted(x , key=lambda y: (y[1]))
#     x[::-1]
    
#     print(x)

# tupleSort()