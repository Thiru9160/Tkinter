#panedwindow:It is widget which acts as container which allows you to organizes other widgets.provides adujstable panes betwwen them.
import tkinter as tk
from tkinter import *
top=tk.Tk()
top.title("Panedwindow example")

#create a panedwindow
panewindow=PanedWindow(top,orient=HORIZONTAL)
panewindow.pack(fill=BOTH,expand=1)

#create left and right panes(frames)
left=Frame(panewindow,bg="lightblue",width=200,height=200)
right=Frame(panewindow,bg="lightgreen",width=200,height=200)

#add the panes to panedwindow
panewindow.add(left)
panewindow.add(right)

#add labels for left and right panes
left_label=Label(left,text="LEFT PANE",bg="lightblue")
left_label.pack()
right_label=Label(right,text="RIGHT PANE",bg="lightgreen")
right_label.pack()

top.mainloop()