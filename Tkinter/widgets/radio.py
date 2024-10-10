import tkinter as tk
from tkinter import messagebox

#Set up the main application window
top = tk.Tk()
top.title("Radio Button Example")
top.geometry("500x500")

#Create a Tkinter variable to store the selected value
radio_var = tk.IntVar()

#Create radio buttons
radio_button1 = tk.Radiobutton(top, text="Male", variable=radio_var, value="Option 1")
radio_button2 = tk.Radiobutton(top, text="Female", variable=radio_var, value="Option 2")
radio_button3 = tk.Radiobutton(top, text="Others", variable=radio_var, value="Option 3")

#place radiobuttons
radio_button1.pack()
radio_button2.pack()
radio_button3.pack()

# Run the application
top.mainloop()