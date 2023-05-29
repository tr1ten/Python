"""
select value from list
contains multiple strings
"""



from tkinter import *

top = Tk()
Lb = Listbox()
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Any other')
Lb.pack(padx=10, pady=10)
top.mainloop()
