import tkinter as tk
import math

def button_click(number):
    current = entry.get()
    entry.delete(0, "end")
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, "end")

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, "end")
        entry.insert(0, result)
    except:
        entry.delete(0, "end")
        entry.insert(0, "Hata")

memory = 0
memory_stored = False  

def memory_clear():
    global memory
    global memory_stored
    memory = 0
    memory_stored = False

def memory_add():
    global memory
    global memory_stored
    try:
        value = float(entry.get())
        memory += value
        memory_stored = True
    except:
        entry.delete(0, "end")
        entry.insert(0, "Hata")

def memory_subtract():
    global memory
    global memory_stored
    try:
        value = float(entry.get())
        memory -= value
        memory_stored = True
    except:
        entry.delete(0, "end")
        entry.insert(0, "Hata")

def memory_recall():
    global memory_stored
    if memory_stored:
        entry.delete(0, "end")
        entry.insert(0, memory)

def factorial():
    try:
        value = int(entry.get())
        result = math.factorial(value)
        entry.delete(0, "end")
        entry.insert(0, result)
    except:
        entry.delete(0, "end")
        entry.insert(0, "Hata")

def absolute_value():
    try:
        value = float(entry.get())
        result = abs(value)
        entry.delete(0, "end")
        entry.insert(0, result)
    except:
        entry.delete(0, "end")
        entry.insert(0, "Hata")

root = tk.Tk()
root.title("Hesap Makinesi")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

memory_label = tk.Label(root, text="Memory: 0", padx=20)
memory_label.grid(row=0, column=4, columnspan=2)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "MC", "M+", "M-", "MR",
    "C", "!", "|x|"
]

row_num, col_num = 1, 0

for button in buttons:
    if button == "=":
        tk.Button(root, text=button, padx=20, pady=20, command=calculate).grid(row=row_num, column=col_num)
    elif button in ["MC", "M+", "M-", "MR", "C", "!"]:
        if button == "MC":
            tk.Button(root, text=button, padx=20, pady=20, command=memory_clear).grid(row=row_num, column=col_num)
        elif button == "M+":
            tk.Button(root, text=button, padx=20, pady=20, command=memory_add).grid(row=row_num, column=col_num)
        elif button == "M-":
            tk.Button(root, text=button, padx=20, pady=20, command=memory_subtract).grid(row=row_num, column=col_num)
        elif button == "MR":
            tk.Button(root, text=button, padx=20, pady=20, command=memory_recall).grid(row=row_num, column=col_num)
        elif button == "C":
            tk.Button(root, text=button, padx=20, pady=20, command=clear).grid(row=row_num, column=col_num)
        elif button == "!":
            tk.Button(root, text=button, padx=20, pady=20, command=factorial).grid(row=row_num, column=col_num)
    elif button == "|x|":
        tk.Button(root, text=button, padx=20, pady=20, command=absolute_value).grid(row=row_num, column=col_num)
    else:
        tk.Button(root, text=button, padx=20, pady=20, command=lambda button=button: button_click(button)).grid(row=row_num, column=col_num)
    
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

root.mainloop()
