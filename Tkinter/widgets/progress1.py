import tkinter as tk
from tkinter import *
from tkinter import ttk
top=tk.Tk()
top.title("progressbar example")
top.geometry("500x500")
#create progressbar widget
progress=ttk.Progressbar(top,orient="vertical",length=300,mode="indeterminate")
#we know the start and end points of progress
progress.pack()
def start_indeterminate():
    progress.start(10)
def stop_indeterminate():
    progress.stop()
start_button=Button(top,text="Start Progress",command=start_indeterminate).pack()
end_button=Button(top,text="Stop Progress",command=stop_indeterminate).pack()
top.mainloop()

