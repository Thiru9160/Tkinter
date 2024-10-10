#unmapping:It's simply hiding the widgets(label,button,entry)
#mapping:after hiding we can retriveal widgets
#umapping depends whether what layout we are using(pack,grid,place)
#widget.layout_forget()
import tkinter as tk 
from tkinter import *
top=tk.Tk()
top.title("pack unmap example")
top.geometry("500x500")

#create a label
label=Label(top,text="hello,I'm packed")
label.pack()

#function for unmap the label
def hide_label():
    label.pack_forget()#unmaps the label from the window
#showing(mapping) the label
def  show_label():
    label.pack()#maps the label to the window

#create button to unmap and map 
hide_button=Button(top,text="HIDE LABEL",command=hide_label)
hide_button.pack()

show_button=Button(top,text="show label",command=show_label)
show_button.pack()

top.mainloop()
