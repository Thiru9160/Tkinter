#toplevel: It is a widget is used to create a window(child window) which is addition to main window(root window)
import  tkinter as tk
from tkinter import *
top=tk.Tk()
top.title("main window")
top.geometry("500x500")


#create a toplevel window (child window)
child=Toplevel(top)
child.title("child window")
child.geometry("250x250")
#add a label
label1=Label(child,text="this child window")
label1.pack()



top.mainloop()
