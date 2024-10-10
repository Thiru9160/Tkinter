import tkinter as tk
# Define the main application window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry('500x500')#window size
# Define the function to perform calculations
def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2
        else:
            result = "Invalid Operation"
        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Invalid input. Please enter numeric values.")
    except ZeroDivisionError:
        result_label.config(text="can't divide by zero")


# Create Entry widgets for input
entry1 = tk.Entry(root)#input to user
entry2 = tk.Entry(root)#to get number 2

# Create buttons for operations
add_button = tk.Button(root, text="+", command=lambda: calculate('add'))
subtract_button = tk.Button(root, text="-", command=lambda: calculate('subtract'))
multiply_button = tk.Button(root, text="*", command=lambda: calculate('multiply'))
divide_button = tk.Button(root, text="/", command=lambda: calculate('divide'))

# Create a label to display the result
result_label = tk.Label(root, text="Result: ")


# Arrange the widgets in a grid
entry1.grid(row=0, column=2,padx=5,pady=5)#pack,place
entry2.grid(row=0, column=4,padx=10,pady=5)

add_button.grid(row=1, column=0)
subtract_button.grid(row=1, column=2)
multiply_button.grid(row=1, column=4)
divide_button.grid(row=1, column=6)

result_label.grid(row=2, column=0,columnspan=6)
# Start the main event loop
root.mainloop()#start our window
