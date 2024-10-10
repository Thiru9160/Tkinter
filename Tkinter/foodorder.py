import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import PhotoImage
top=tk.Tk()
top.title("Food ordering App")
top.geometry("500x500")
#create a menu items and their price
menu={
    "Pizza":8.99,
    "Burger":5.99,
    "Pasta":6.99,
    "Salad":4.99,
    "soda":1.99
}
#initialize the selected items list
selected_items=[]

#function for DarkMode
def dark_mode():
    if dark_mode_var.get():
        top.config(bg="black")
        for widget in top.winfo_children():
            widget.config(bg="black",fg="white")
    else:
        top.config(bg="white")
        for widget in top.winfo_children():
            widget.config(bg="white",fg="black")

#function to update the total price
def update_total():
    total=sum(menu[item]*qty for item,qty in selected_items)
    total_label.config(text=f"Total: ${total:.2f}")

#function to add an item to the selection with quantity
def add_item(item,quantity_entry):
    try:
        qty=int(quantity_entry.get())
        if qty>0:
            selected_items.append((item,qty))
            update_total()
            update_selection_list()
    except IndexError:
        pass

#function to clear all seleected items
def clear_selection():
    selected_items.clear()
    update_total()
    update_selection_list()

#function to update selection list
def update_selection_list():
    selection_list.delete(0,END)
    for item,qty in selected_items:
        selection_list.insert(END,f"{item}x{qty}")
#function to submit order
def submit_order():
    if not selected_items:
        messagebox.showinfo("order submission","No item is selected.")
        return
    total=sum(menu[item]*qty for item,qty in selected_items)
    messagebox.showinfo("order Submission",f"Order Submitted!\nTotal:${total:.2f}")
    clear_selection()
def remove_item():
    try:
        selected=selection_list.curselection()
        if selected:
            index=selected[0]
            del selected_items[index]
            update_total()
            update_selection_list()
    except IndexError:
        pass


#load all images
pizza_img=PhotoImage(file="pizaa.png").subsample(20,20)
pasta_img=PhotoImage(file="pasta.png").subsample(20,20)
salad_img=PhotoImage(file="salad.png").subsample(20,20)
soda_img=PhotoImage(file="soda.png").subsample(20,20)
burger_img=PhotoImage(file="burger.png").subsample(20,20)
#mapping the images with food names
images={
    "Pizza":pizza_img,
    "Burger":burger_img,
    "Pasta":pasta_img,
    "Salad":salad_img,
     "soda":soda_img

} 
#add items with quantity selectors
row=0
for item,price in menu.items():
    img_label=Label(top,image=images[item])
    img_label.grid(row=row,column=0)
    label1=Label(top,text=f"{item} - ${price:.2f}")
    label1.grid(row=row,column=1)
    
    quantity_entry=Entry(top)
    quantity_entry.grid(row=row,column=2)

    add_button=Button(top,text="ADD",command=lambda item=item,entry=quantity_entry:add_item(item,entry))
    add_button.grid(row=row,column=3)
    row+=1
#add selected items list
selected_label=Label(top,text="Selected items:")
selected_label.grid(row=0,column=4)

selection_list=Listbox(top)
selection_list.grid(row=1,column=4,rowspan=5,padx=30,pady=30)

#Add buttons for removing ,clearing and submitting
remove_button=Button(top,text="Removed Selected item",command=remove_item)
remove_button.grid(row=6,column=4)

clear_button=Button(top,text="Clear All",command=clear_selection)
clear_button.grid(row=7,column=4)

submit_button=Button(top,text="Submit Order",command=submit_order)
submit_button.grid(row=8,column=4)

#Add a label to dispaly the total price
total_label=Label(top,text="Total: $0.00")
total_label.grid(row=9,column=4)

dark_mode_var=tk.BooleanVar()
dark_mode_checbox=Checkbutton(top,text="Dark mode",variable=dark_mode_var,command=dark_mode)
dark_mode_checbox.grid(row=10,column=1)


top.mainloop()
