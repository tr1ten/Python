# -*- coding: utf-8 -*-
"""
Draw label and textbox on window

Label arguments

window = parent of label
text = "display string"

pack and grid methods are used to show labels on main window

grid has 2 arguments

row and column 

because screen is a grid of rows and columns

"""


from tkinter import *

window = Tk();
window.title("Main window");

Label(window, text = "First Name").grid(row=0);
Label(window, text = "Laste Name").grid(row=1);

e1 = Entry(window);
e2 = Entry(window);

e1.grid(row = 0, column = 1);
e2.grid(row = 1, column = 1);

window.mainloop();