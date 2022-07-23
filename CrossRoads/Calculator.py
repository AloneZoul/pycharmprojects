from tkinter import *


def button_click(number):
    enum = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(enum) + str(number))


def button_clear():
    entry.delete(0, END)


def button_add():
    first_num = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    entry.delete(0, END)


def button_min():
    first_num = entry.get()
    global f_num
    global math
    math = "substraction"
    f_num = int(first_num)
    entry.delete(0, END)




def button_equal():
    second_num = entry.get()
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, f_num + int(second_num))
    if math=="substraction":
        entry.insert(0,f_num-int(second_num))

Frame = Tk()
Frame.title("CALCULATOR")

entry = Entry(Frame, width=50, borderwidth=5)
entry.grid(row=0, column=0, columnspan=8, padx=10, pady=5)

# define your button

button_1 = Button(Frame, padx=15, pady=15, text="1", command=lambda: button_click(1))
button_2 = Button(Frame, padx=15, pady=15, text="2", command=lambda: button_click(2))
button_3 = Button(Frame, padx=15, pady=15, text="3", command=lambda: button_click(3))
button_4 = Button(Frame, padx=15, pady=15, text="4", command=lambda: button_click(4))
button_5 = Button(Frame, padx=15, pady=15, text="5", command=lambda: button_click(5))
button_6 = Button(Frame, padx=15, pady=15, text="6", command=lambda: button_click(6))
button_7 = Button(Frame, padx=15, pady=15, text="7", command=lambda: button_click(7))
button_8 = Button(Frame, padx=15, pady=15, text="8", command=lambda: button_click(8))
button_9 = Button(Frame, padx=15, pady=15, text="9", command=lambda: button_click(9))
button_0 = Button(Frame, padx=15, pady=15, text="0", command=lambda: button_click(0))

button_add = Button(Frame, padx=15, pady=15, text="+", command=button_add)
button_clear = Button(Frame, padx=30, pady=15, text="Clear", command=button_clear)
button_equal = Button(Frame, padx=30, pady=15, text="=", command=button_equal)
button_min = Button(Frame, padx=15, pady=15, text="-", command=button_min)

# place button on the screen

button_1.grid(row=3, column=0, pady=10)
button_2.grid(row=3, column=1, pady=10)
button_3.grid(row=3, column=2, pady=10)

button_4.grid(row=2, column=0, pady=10)
button_5.grid(row=2, column=1, pady=10)
button_6.grid(row=2, column=2, pady=10)

button_7.grid(row=1, column=0, pady=10)
button_8.grid(row=1, column=1, pady=10)
button_9.grid(row=1, column=2, pady=10)

button_0.grid(row=4, column=0, pady=10)

button_add.grid(row=2, column=3, pady=10)
button_clear.grid(row=4, column=1, pady=10, columnspan=2)
button_equal.grid(row=4, column=2, pady=10, columnspan=6)
button_min.grid(row=3, column=3, pady=10)

Frame.mainloop()
