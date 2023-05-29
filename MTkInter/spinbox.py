"""
spinbox

contains two buttons 
up to increase values
down to decrease values
"""

from tkinter import *
master = Tk()
w = Spinbox(master, from_ = 0, to = 10)
w.pack()
mainloop()
