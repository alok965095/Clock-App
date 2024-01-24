from tkinter import*
from tkinter.ttk import*
from time import strftime

root=Tk()
root.title("Clock")
root.resizable(False,False)
def none():
    text=strftime("%H:%M:%S %p")
    lbl.config(text=text)
    lbl.after(1000,none)
lbl=Label(root,font=("digital-7",50,"bold"),
    background="black",foreground="red")

def c1():
    lbl.config(background="white",foreground="black")
def defa():
    lbl.config(background="black",foreground="red")
def c2():
    lbl.config(background="green",foreground="red")
def c3():
    lbl.config(background="green",foreground="blue")
def c4():
    lbl.config(background="red",foreground="blue")
def c5():
    lbl.config(background="red",foreground="black")
def exit():
    root.destroy()
man = Menu(root)
m1 = Menu(man,tearoff=0)
m1.add_command(label="CLASIC",command=c1)
m1.add_command(label="Default",command=defa)
m1.add_separator()
m1.add_command(label="RED AND GREEN",command=c2)
m1.add_command(label="BLUE AND GREEN",command=c3)
m1.add_command(label="BLUE AND RED",command=c4)
m1.add_command(label="RED AND BLACK",command=c5)
m1.add_separator()
m1.add_command(label="Exit",command=exit)
man.add_cascade(label="Theme",menu=m1)
root.config(menu=man)


lbl.pack(anchor="center")
none()
root.mainloop()