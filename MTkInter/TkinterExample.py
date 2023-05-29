"""
Draw button and destroy window on click

arguments of button

window = where to place button
text = "display value on button"
width = width of button
command = action when button clicked


Tk()    is our main window

window.mainloop() is necessary in each program

pack() is used to show button on window
"""




from tkinter import *

window = Tk();
window.title("Main window");

button = Button(window, text = "Stop", width = 25, command = window.destroy);
button.pack();
window.mainloop();