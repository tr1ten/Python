import tkinter as tk
from tkinter import messagebox
import string
window = tk.Tk()
window.title("Auth Screen")
err = tk.Label()
def validate(mail:str):
    print("validating ",mail)
    if any([1 for x in mail if x not in (string.ascii_letters + "@")]): return 0
    return 1
def showError(msg):
    err['text'] = msg
txt = tk.Label(text="Signin",padx=100,font=('Aria',20))
txt.grid(row=1)

fn  = tk.Entry(width=20,validate="key",
               validatecommand=(window.register(validate),"%P"),
               invalidcommand=(window.register(lambda :showError("Only @ and alphabets allowed!")),))
fn.insert(0, 'email')
fn.grid(columnspan=2, row=2)

ln  = tk.Entry(width=20)
ln.grid(columnspan=2,row=3)
ln.insert(0, 'password')

err.grid(row=4)

selected = tk.IntVar()
rad1 = tk.Radiobutton(window,text='female', value=0, variable=selected)
rad2 = tk.Radiobutton(window,text='male', value=1, variable=selected)
rad1.grid(column = 0, row = 5)
rad2.grid(column = 1, row = 5)


def callback():
    # show greeting
    messagebox.showinfo(title="Greetnigs",message=f"hi, {fn.get()} ")
btn = tk.Button(command=callback,text="Login")
btn.grid(row=6)
window.mainloop()

