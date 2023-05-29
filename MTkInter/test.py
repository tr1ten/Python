import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("Auth Screen")
txt = tk.Label(text="Signin",padx=100,font=('Aria',20))
txt.grid(row=1)
fn  = tk.Entry(width=20)
fn.grid(columnspan=2, row=2)

ln  = tk.Entry(width=20)
ln.grid(columnspan=2,row=3)
def callback():
    # show greeting
    messagebox.showinfo(title="Greetnigs",message=f"hi, {fn.get()} {ln.get()}")
btn = tk.Button(command=callback,text="Login")
btn.grid(row=4)
window.mainloop()

