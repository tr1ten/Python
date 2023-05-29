# -*- coding: utf-8 -*-
"""
slider is used to set value of variable from slider with in a range

from = start of range
to = end of range

orientation = HORIZONTAL or Vertical , default is Vertical
"""


from tkinter import *

window = Tk();
window.title("Main window");

w = Scale(window, from_ = 0, to_ = 200);
w.pack();

w = Scale(window, from_ = 0, to_ = 200, orient = HORIZONTAL);
w.pack();

window.mainloop();