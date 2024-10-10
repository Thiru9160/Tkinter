import tkinter as tk
from  tkinter import  filedialog
from tkinter import messagebox
from tkinter import *
#main application
top=tk.Tk()
top.title("menu example")
top.iconbitmap("marshall_paw_patrol_canine_patrol_icon_263825.ico")
top.geometry("500x500")
#create new file
def save_file():
    file_content=text_area.get("1.0",tk.END)
    file_path=filedialog.askopenfilename(defaultextension=".txt",filetypes=[("Text files","*.txt"),("All files","*.*")])
    if file_path:
        try:
            with open(file_path,"w") as file:
                file.write(file_content)
            messagebox.showinfo("Success","File Saved successfully!")
        except Exception as e:
            messagebox.showerror("Error",f"failed to save file:\n{e}")
text_area=tk.Text(top,wrap=tk.WORD,undo=True)
text_area.pack()

def open_file():
    file_path=filedialog.askopenfilename(title="open file",filetypes=(("text files",".txt"),("All Files","*.*")))
    if file_path:
        with open(file_path,"r") as file:
            file_content=file.read()
            messagebox.showinfo("File content",file_content)

#function to print message
def show_message(title,message):
    messagebox.showinfo(title,message)

#create a menubar
menu_bar=tk.Menu(top)
#create a file menu
file_menu=tk.Menu(menu_bar,tearoff=0)
file_menu.add_command(label="new",command=save_file)
file_menu.add_command(label="open",command=open_file)
file_menu.add_command(label="save",command=lambda :show_message("Save","Save file"))
file_menu.add_separator()
file_menu.add_command(label="exit",command=lambda:show_message("exit","exit action"))

menu_bar.add_cascade(label="file",menu=file_menu)

#create view menu
view_menu=tk.Menu(menu_bar,tearoff=0)
view_menu.add_command(label='tool windows',command=lambda :show_message("Tools","Tools windows"))
view_menu.add_command(label='edit',command=lambda :show_message("edit","edit action"))
view_menu.add_command(label='copy',command=lambda :show_message("copy","copy action"))

menu_bar.add_cascade(label='view',menu=view_menu)
#Exit button
btn_exit=Button(top,text="Exit",command=top.quit)
btn_exit.pack()

#add menu_bar to top window
top.config(menu=menu_bar)

#run application
top.mainloop()

