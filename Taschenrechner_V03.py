# ToDo: GUI erstellen

# ToDo: Ideen:
# ToDo: 1. Anstelle von Entry und Output in der GUI sonst in der Konsole?

import tkinter as tk

#functions for the buttons of the

output = ""
def plus():
    input_field.insert(tk.END,"+")

def minus():
    input_field.insert(tk.END,"-")

def multiplicator():
    input_field.insert(tk.END,"*")

def potentiate():
    input_field.insert(tk.END, "**")

def open_bracket():
    input_field.insert(tk.END,"(")

def close_bracket():
    input_field.insert(tk.END, ")")

def division():
    input_field.insert(tk.END,"/")

def rest():
    input_field.insert(tk.END,"%")

def full_delete():
    input_field.delete(0, tk.END)
    output_field.config(text="")

def partial_delete():
    input_field.delete(input_field.index("end") - 1)

def n_0():
    input_field.insert(tk.END, 0)
def n_1():
    input_field.insert(tk.END, 1)

def n_2():
    input_field.insert(tk.END, 2)

def n_3():
    input_field.insert(tk.END, 3)

def n_4():
    input_field.insert(tk.END, 4)

def n_5():
    input_field.insert(tk.END, 5)

def n_6():
    input_field.insert(tk.END, 6)

def n_7():
    input_field.insert(tk.END, 7)

def n_8():
    input_field.insert(tk.END, 8)

def n_9():
    input_field.insert(tk.END, 9)

output = ""
def equal():
    middle = input_field.get()
    output = eval(middle)
    output_field.config(text=output)

#tkinter window

window = tk.Tk()

title = tk.Label(text="Welcome to my calculator!\n\nLet the math begin. ",
                 background = "#bdc7be",
                 foreground = "#111211",
                 width = 37,
                 height = 5
                 )

#input field

input_field = tk.Entry(window,
                       width = 17,
                       justify = "center",
                       font = ("Arial", 20))

#output field

output_field = tk.Label(text = output,
                        font = ("bold")
                        )

#operator buttons

equal_button = tk.Button(text = "=",
                         width = "8",
                         height = "3",
                         background = "#bdc7be",
                         command = equal
                         )

plus_button = tk.Button(text = "+",
                        width = "8",
                        height = "3",
                        background = "#bdc7be",
                        command = plus
                        )

minus_button = tk.Button(text= "-",
                         width = "8",
                         height = "3",
                         background = "#bdc7be",
                         command = minus
                         )

multiplicator_button = tk.Button(text="*",
                                 width = "8",
                                 height = "3",
                                 background = "#bdc7be",
                                 command = multiplicator
                                 )

division_button = tk.Button(text = "/",
                            width = "8",
                            height = "3",
                            background = "#bdc7be",
                            command = division
                            )

rest_button = tk.Button(text = "Rest",
                        width = "8",
                        height = "3",
                        background = "#bdc7be",
                        command= rest
                        )

full_delete_button = tk.Button(text = "C",
                          width = "8",
                          height = "3",
                          background = "#bdc7be",
                          command = full_delete
                          )

potentiate_button = tk.Button(text = "^",
                              width = "8",
                              height = "3",
                              background = "#bdc7be",
                              command = potentiate
                              )

open_bracket_button = tk.Button(text="(",
                                width = "8",
                                height = "3",
                                background = "#bdc7be",
                                command = open_bracket
                                )

closing_bracket_button = tk.Button(text=")",
                                   width = "8",
                                   height = "3",
                                   background = "#bdc7be",
                                   command = close_bracket
                                   )

del_button = tk.Button(text="Del",
                       width = "8",
                       height = "3",
                       background = "#bdc7be",
                       command = partial_delete
                       )

#number buttons

number_0 = tk.Button(text="0",
                     width = "8",
                     height = "3",
                     background = "#b3b5ac",
                     command = n_0
                     )

number_1 = tk.Button(text="1",
                     width = "8",
                     height = "3",
                     background = "#b3b5ac",
                     command = n_1
                     )

number_2 = tk.Button(text="2",
                     width = "8",
                     height = "3",
                     background = "#b3b5ac",
                     command = n_2
                     )

number_3 = tk.Button(text="3",
                     width = "8",
                     height = "3",
                     background = "#b3b5ac",
                     command = n_3
                     )

number_4 = tk.Button(text="4",
                     width = "8",
                     height = "3",
                     background = "#b3b5ac",
                     command = n_4
                     )

number_5 = tk.Button(text="5",
                     width = "8",
                     height = "3",
                     background = "#b3b5ac",
                     command = n_5
                     )

number_6 = tk.Button(text="6",
                     width = "8",
                     height = "3",
                     background = "#b3b5ac",
                     command = n_6
                     )

number_7 = tk.Button(text="7",
                     width = "8",
                     height = "3",
                     background = "#b3b5ac",
                     command = n_7
                     )

number_8 = tk.Button(text="8",
                     width = "8",
                     height = "3",
                     background = "#b3b5ac",
                     command = n_8
                     )

number_9 = tk.Button(text="9",
                     width = "8",
                     height = "3",
                     background = "#b3b5ac",
                     command= n_9
                     )

#graphical interface/grid of buttons

title.grid(row=0, column=0, columnspan=4)

#input field

input_field.grid(row=1, column=0, columnspan=4)

#output field

output_field.grid(row=2, column=0, columnspan=4)
#buttons

number_7.grid(row=3, column=0)
number_8.grid(row=3, column=1)
number_9.grid(row=3, column=2)
plus_button.grid(row=3, column=3)
number_4.grid(row=4, column=0)
number_5.grid(row=4, column=1)
number_6.grid(row=4, column=2)
minus_button.grid(row=4, column=3)
number_1.grid(row=5, column=0)
number_2.grid(row=5, column=1)
number_3.grid(row=5, column=2)
multiplicator_button.grid(row=5, column=3)
number_0.grid(row=6, column=0)
open_bracket_button.grid(row=6, column=1)
closing_bracket_button.grid(row=6, column=2)
division_button.grid(row=6, column=3)
rest_button.grid(row=7, column=0)
del_button.grid(row=7, column=1)
full_delete_button.grid(row=7, column=2)
equal_button.grid(row=7, column=3)


window.mainloop()