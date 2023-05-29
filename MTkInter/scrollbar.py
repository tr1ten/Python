"""
add scrollbar to list box


"""


from tkinter import *
root = Tk()
scrollbar = Scrollbar(root)
"""show scrollbar"""
scrollbar.pack( side = RIGHT, fill = Y )
"""create list and add scrollbar"""
mylist = Listbox(root, yscrollcommand = scrollbar.set )


"""add 100 items to list"""
for line in range(100):
    mylist.insert(END, 'This is line number' + str(line))
"""show list on screen"""
mylist.pack( side = LEFT, fill = BOTH )
"""scroll list values when scrollbar is scrolled"""
scrollbar.config( command = mylist.yview )
mainloop()
