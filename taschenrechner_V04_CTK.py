import customtkinter

#functions for the buttons of the
"""
output = ""
def plus():
    input_field.insert(CTk.END,"+")

def minus():
    input_field.insert(CTk.END,"-")

def multiplicator():
    input_field.insert(CTk.END,"*")

def potentiate():
    input_field.insert(CTk.END, "**")

def open_bracket():
    input_field.insert(CTk.END,"(")

def close_bracket():
    input_field.insert(CTk.END, ")")

def division():
    input_field.insert(CTk.END,"/")

def rest():
    input_field.insert(CTk.END,"%")

def full_delete():
    input_field.delete(0, CTk.END)
    output_field.config(text="")

def partial_delete():
    input_field.delete(input_field.index("end") - 1)

def n_0():
    input_field.insert(CTk.END, 0)
def n_1():
    input_field.insert(CTk.END, 1)

def n_2():
    input_field.insert(CTk.END, 2)

def n_3():
    input_field.insert(CTk.END, 3)

def n_4():
    input_field.insert(CTk.END, 4)

def n_5():
    input_field.insert(CTk.END, 5)

def n_6():
    input_field.insert(CTk.END, 6)

def n_7():
    input_field.insert(CTk.END, 7)

def n_8():
    input_field.insert(CTk.END, 8)

def n_9():
    input_field.insert(CTk.END, 9)

output = ""
def equal():
    middle = input_field.get()
    output = eval(middle)
    output_field.config(text=output)
"""
# window setup

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
window.geometry("430x350")

window.title("Wilkommen in meinem Taschenrechner!")

# input field

input_field = customtkinter.CTkEntry(master = window,
                                     width = 410,
                                     justify = "center",
                                     font = ("Arial", 20))

#output field

output_frame = customtkinter.CTkFrame(master = window,
                                      width = 410,
                                      height = 60,
                                      fg_color = "#383838")

output_field = customtkinter.CTkLabel(output_frame,
                                      #text = output,
                                      width = 390
                                      )

#operator buttons

equal_button = customtkinter.CTkButton(master = window,
                                       text = "=",
                                       width = "8",
                                       height = "3",
                                       #command = equal
                                       )

plus_button = customtkinter.CTkButton(master = window,
                                      text = "+",
                                      width = "8",
                                      height = "3",
                                      #command = plus
                                      )

minus_button = customtkinter.CTkButton(master = window,
                                       text= "-",
                                       width = "8",
                                       height = "3",
                                       #command = minus
                                       )

multiplicator_button = customtkinter.CTkButton(master = window,
                                               text="*",
                                               width = "8",
                                               height = "3",
                                               #command = multiplicator
                                               )

division_button = customtkinter.CTkButton(master = window,
                                          text = "/",
                                          width = "8",
                                          height = "3",
                                          #command = division
                                          )

rest_button = customtkinter.CTkButton(master = window,
                                      text = "Rest,",
                                      width = "8",
                                      height = "3",
                                      #command= rest
                                      )

full_delete_button = customtkinter.CTkButton(master = window,
                                             text = "C",
                                             width = "8",
                                             height = "3",
                                             #command = full_delete
                                             )

potentiate_button = customtkinter.CTkButton(master = window,
                                            text = "^",
                                            width = "8",
                                            height = "3",
                                            #command = potentiate
                                            )

open_bracket_button = customtkinter.CTkButton(master = window,
                                              text="(",
                                              width = "8",
                                              height = "3",
                                              #command = open_bracket
                                              )

closing_bracket_button = customtkinter.CTkButton(master = window,
                                                 text=")",
                                                 width = "8",
                                                 height = "3",
                                                 #command = close_bracket
                                                 )

del_button = customtkinter.CTkButton(master = window,
                                     text="Del",
                                     width = "8",
                                     height = "3",
                                     #command = partial_delete
                                     )

#define grid

window.columnconfigure((0,1,2,3), weight = 0)
window.rowconfigure((0,1,2,3), weight = 0)

#input field

input_field.grid(row = 0, column = 0, padx = 10, pady = 10)
output_frame.grid(row = 1, column = 0, padx = 10, pady = 5)
output_field.grid(row=1, column = 0, padx = 10, pady = 5)

# buttons
"""
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
"""

window.mainloop()