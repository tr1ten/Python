from tkinter import *
import tkinter.messagebox as mt


root = Tk()

menu = Menu()
root.config(menu=menu)
helpmenu = Menu(menu)
menu.add_cascade(label="help",menu=helpmenu)
menu.add_cascade(label="about")

helpmenu.add_command(label="Exit",command=root.destroy)


root.title("Registration Form")
l1 =    Label(root,text="Register Form",bg="yellow",font=('Courier',23,'normal'))
l1.grid(row=1,columnspan=3)
mail = StringVar();
l2 = Label(root,text="Mail ")
l2.grid(row=2,column=0)
e1 = Entry(root,textvariable=mail)
e1.grid(row=2,column=1)

passw = StringVar()
l3 = Label(root,text="Password ")
l3.grid(row=3,column=0)
e2 = Entry(root,show="*",textvariable=passw)
e2.grid(row=3,column=1)

# w = Scale(window, from_ = 0, to_ = 200);
# w.pack();

l4 = Label(root,text="Salary ")
l4.grid(row=4,column=0)
sw = Spinbox(from_=0,to=1000)
sw.grid(row=4,column=1)

l4 = Label(root,text="Gender ")
l4.grid(row=5,column=0)
gender = StringVar()
gender.set("Male")
options = ["Male","Female","Ravi"]
gw = OptionMenu(root,gender,*options);
gw.grid(row=5,column=1,rowspan=2)

m = StringVar()
rem = BooleanVar()
Checkbutton(root,text="remember me",variable=rem).grid(row=7,column=1)

msg = Label(root,textvariable=m)
def onSubmit():
    print("on submit ",mail.get(),passw.get())
    if not mail.get() or not passw.get():
        mt.showerror("Error","Invalid password or mail")
    else:
        if rem.get():
            with open("db.txt",'a+') as f:
                f.write(str({
                    'mail':mail.get(),
                    'password':passw.get()
                }));
        m.set("Register Succesfully")


msg.grid(row=8,column=1)
sw = Button(root,text="Login",command=onSubmit)
sw.grid(row=9,column=2)


mainloop()