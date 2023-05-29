# -*- coding: utf-8 -*-
"""
radio button

only one button will be selected at a time

value of variable v will be 1 or 2 at a time

pack is used to display

"""


from tkinter import *

window = Tk();
window.title("Main window");

v = IntVar();
Radiobutton(window, text = "ABC", variable = v, value = 1).pack();
Radiobutton(window, text = "XYZ", variable = v, value = 2).pack();

window.mainloop();