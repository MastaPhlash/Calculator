import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        op = operation.get()
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Simple Calculator")

    tk.Label(root, text="First Number:").grid(row=0, column=0)
    entry_num1 = tk.Entry(root)
    entry_num1.grid(row=0, column=1)

    tk.Label(root, text="Operation:").grid(row=1, column=0)
    operation = tk.StringVar(value='+')
    tk.OptionMenu(root, operation, '+', '-', '*', '/').grid(row=1, column=1)

    tk.Label(root, text="Second Number:").grid(row=2, column=0)
    entry_num2 = tk.Entry(root)
    entry_num2.grid(row=2, column=1)

    tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)
    label_result = tk.Label(root, text="Result: ")
    label_result.grid(row=4, column=0, columnspan=2)

    root.mainloop()