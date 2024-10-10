import tkinter as tk
from tkinter import *
#create main application window
top=tk.Tk()
top.title("Frames in tkinter")
top.geometry("500x500")
#create a top frame
top_frame=Frame(top,bg="lightblue")
top_frame.pack(side=TOP,fill=BOTH,expand=True)
#create a bottom frame
bottom_frame=Frame(top,bg="lightgreen")
bottom_frame.pack(side=BOTTOM,fill=BOTH,expand=True)
#create a button
btn1=Button(top_frame,text="submit")
btn1.pack()
btn2=Button(bottom_frame,text="submit2")
btn2.pack()






#start main application
top.mainloop()