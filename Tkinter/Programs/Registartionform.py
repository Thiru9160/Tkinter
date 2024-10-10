import tkinter as tk
from tkinter import *
from tkinter import messagebox

#create main window
top=tk.Tk()
top.title("Registration Form")
top.geometry("500x500")

#create a function to handle form submission
def submit_form():
    #get the values from entries
    first_name=entry_FN.get()
    last_name=entry_LN.get()
    email=entry_email.get()
    password=entry_password.get()
    gender=gender_var.get()
    agreed=var1.get()

    if not first_name or not last_name or not email or not gender or not password or not agreed:
        messagebox.showwarning("Warning","ALL FIELDS ARE REQUIRED!")
        return
    messagebox.showinfo("Registration Successful",f"First Name:{first_name}\nLast Name:{last_name}\nEmail:{email}\nPassword:{password},Gender:{gender}")



#Create labels for firstname
label1=tk.Label(top,text="First Name:",bg="yellow",fg="red",font=("Arial",14))
#label1.config(text="Name",fg="blue")
#label1["bg"]="red"
entry_FN=tk.Entry(top)
#Create labels for LastName
label2=tk.Label(top,text="Last Name:",fg="red",bg="blue")
#label2["text"]="LN"
entry_LN=tk.Entry(top)
#Create labels Email
label3=tk.Label(top,text="Email:")
entry_email=tk.Entry(top)
#Create labels Password
label4=tk.Label(top,text="Password:")
entry_password=tk.Entry(top,show="*")
#radiobutton for gender
label5=tk.Label(top,text="Gender:")
gender_var=tk.StringVar(value="")
radio_button1 = tk.Radiobutton(top, text="Male", variable=gender_var, value="Option 1")
radio_button2 = tk.Radiobutton(top, text="Female", variable=gender_var, value="Option 2")
radio_button3 = tk.Radiobutton(top, text="Others", variable=gender_var, value="Option 3")
#place radiobuttons in window
label5.grid(row=4,column=0)
radio_button1.grid(row=4,column=1,padx=10,pady=10)
radio_button2.grid(row=4,column=2,padx=10,pady=10)
radio_button3.grid(row=4,column=3,padx=20,pady=20)
#create checkbox
var1=tk.BooleanVar()
chk1=tk.Checkbutton(top,text="I have Agreed",variable=var1)
chk1.grid(row=5,column=3)
#submit button
btn1=tk.Button(top,text="submit",command=submit_form,bg="yellow",fg="green")
btn1.grid(row=6,column=3)



#place widgets in main window
label1.grid(row=0,column=0,padx=10,pady=10)
entry_FN.grid(row=0,column=1,padx=10,pady=10)

label2.grid(row=1,column=0,padx=10,pady=10)
entry_LN.grid(row=1,column=1,padx=10,pady=10)

label3.grid(row=2,column=0,padx=10,pady=10)
entry_email.grid(row=2,column=1,padx=10,pady=10)

label4.grid(row=3,column=0,padx=10,pady=10)
entry_password.grid(row=3,column=1,padx=10,pady=10)

#Run the main event loop
top.mainloop()