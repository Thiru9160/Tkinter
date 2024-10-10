#messagebox:it is  a dialog box that is used to display a message to the user.warning,error and information.
import tkinter  as tk
from tkinter import *
from tkinter import messagebox
top=tk.Tk()
top.title("messagebox example")
top.geometry("500x500")
def show_messagebox():
    messagebox.showinfo("information","this is information message")
    messagebox.showwarning("warning","this is warning message")
    messagebox.showerror("error","this is error message")
    #ask a question to user
    response=messagebox.askquestion("question","do you like tkinter")
    if  response=="yes":
        print("user like tkinter")
    else:
        print("user dont like tkinter")
   #ask ok/cancel
    if messagebox.askyesno("yes/no","are you sure?"):
     print("user clicked yes")
    else:
     print("user clicked cancel")
    #ask retry
    if messagebox.askretrycancel("retry","do you want to retry?"):
       print("user clicked retry")
    else:
       print("user clicked cancel")

btn1=Button(top,text="click",command=show_messagebox)
btn1.pack()


top.mainloop()