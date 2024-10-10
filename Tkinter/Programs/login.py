import tkinter as tk
from tkinter import *
from tkinter import messagebox
import subprocess
top=tk.Tk()
top.title("login")
def login():
    username=username_entry.get()
    password=password_entry.get()

    if username=="sidd" and password=="sam":
        messagebox.showinfo("Login Success","Welcome to Food App")
        top.destroy()#close the login page
        subprocess.Popen(['python','calci.py'])#Run the food order code
    else:
        messagebox.showerror("Login Failed","Invalid Details.Please try again")

#create label and entry for username
username_label=Label(top,text="UserName:")
username_label.pack()
username_entry=Entry(top)
username_entry.pack()
#create label and entry for password
password_label=Label(top,text="Password")
password_label.pack()
password_entry=Entry(top,Text="*")
password_entry.pack()
#login button
login_button=Button(top,text="login",command=login)
login_button.pack()


top.mainloop()