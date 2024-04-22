import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Basic Calculator")

e = tk.Entry(root, width=45, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, tk.END)


def button_equal():
    second_number = e.get()
    e.delete(0, tk.END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        if second_number == "0":
            messagebox.showerror("Error", "Division by zero")
        else:
            e.insert(0, f_num / int(second_number))


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, tk.END)


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, tk.END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, tk.END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, tk.END)


# Define buttons
padx, pady = 30, 10
button_1 = tk.Button(root, text="1", padx=padx, pady=pady, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=padx, pady=pady, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=padx, pady=pady, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=padx, pady=pady, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=padx, pady=pady, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=padx, pady=pady, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=padx, pady=pady, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=padx, pady=pady, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=padx, pady=pady, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=padx, pady=pady, command=lambda: button_click(0))
button_add = tk.Button(root, text="+", padx=29, pady=pady, command=button_add)
button_subtract = tk.Button(root, text="-", padx=padx, pady=pady, command=button_subtract)
button_multiply = tk.Button(root, text="*", padx=padx, pady=pady, command=button_multiply)
button_divide = tk.Button(root, text="/", padx=padx, pady=pady, command=button_divide)
button_equal = tk.Button(root, text="=", padx=67, pady=pady, command=button_equal)
button_clear = tk.Button(root, text="Clear", padx=81, pady=pady, command=button_clear)

# Put the buttons on the screen
button_clear.grid(row=1, column=0, columnspan=4, sticky="ew")

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_divide.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_add.grid(row=4, column=3)


button_0.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_subtract.grid(row=5, column=3)

root.mainloop()
