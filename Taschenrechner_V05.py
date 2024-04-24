import customtkinter

#functions for the buttons of the

output = ""


def plus():
    input_field.insert(customtkinter.END,"+")

def minus():
    input_field.insert(customtkinter.END,"-")

def multiplicator():
    input_field.insert(customtkinter.END,"*")

def potentiate():
    input_field.insert(customtkinter.END, "**")

def open_bracket():
    input_field.insert(customtkinter.END,"(")

def close_bracket():
    input_field.insert(customtkinter.END, ")")

def division():
    input_field.insert(customtkinter.END,"/")

def rest():
    input_field.insert(customtkinter.END,"%")

def full_delete():
    input_field.delete(0, customtkinter.END)
    output_field.configure(text="")

def partial_delete():
    input_field.delete(input_field.index("end") - 1)

def n_0():
    input_field.insert(customtkinter.END, 0)

def n_1():
    input_field.insert(customtkinter.END, 1)

def n_2():
    input_field.insert(customtkinter.END, 2)

def n_3():
    input_field.insert(customtkinter.END, 3)

def n_4():
    input_field.insert(customtkinter.END, 4)

def n_5():
    input_field.insert(customtkinter.END, 5)

def n_6():
    input_field.insert(customtkinter.END, 6)

def n_7():
    input_field.insert(customtkinter.END, 7)

def n_8():
    input_field.insert(customtkinter.END, 8)

def n_9():
    input_field.insert(customtkinter.END, 9)

def equal():
    middle = input_field.get()
    output = eval(middle)
    output_field.configure(text=output)


# window setup

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
window.geometry("420x380")

window.title("Wilkommen in meinem Taschenrechner!")

# input field

input_field = customtkinter.CTkEntry(master = window,
                                     width = 390,
                                     height = 40,
                                     justify = "center",
                                     font = ("Arial", 20))

#output field

output_frame = customtkinter.CTkFrame(master = window,
                                      width = 390,
                                      height = 50,
                                      fg_color = "#383838")


output_field = customtkinter.CTkLabel(output_frame,
                                      text = output,
                                      width = 370,
                                      height = 40,
                                      font = ("Arial", 20)
                                      )

#operator buttons

equal_button = customtkinter.CTkButton(master = window,
                                       text = "=",
                                       width = 100,
                                       height = 50,
                                       fg_color = "#545454",
                                       command = equal
                                       )

plus_button = customtkinter.CTkButton(master = window,
                                      text = "+",
                                      width = 100,
                                      height = 50,
                                      fg_color = "#545454",
                                      command = plus
                                      )

minus_button = customtkinter.CTkButton(master = window,
                                       text= "-",
                                       width = 100,
                                       height = 50,
                                       fg_color = "#545454",
                                       command = minus
                                       )

multiplicator_button = customtkinter.CTkButton(master = window,
                                               text="*",
                                               width = 100,
                                               height = 50,
                                               fg_color = "#545454",
                                               command = multiplicator
                                               )

division_button = customtkinter.CTkButton(master = window,
                                          text = "/",
                                          width = 100,
                                          height = 50,
                                          fg_color = "#545454",
                                          command = division
                                          )

rest_button = customtkinter.CTkButton(master = window,
                                      text = "Rest",
                                      width = 100,
                                      height = 50,
                                      fg_color = "#545454",
                                      command= rest
                                      )

full_delete_button = customtkinter.CTkButton(master = window,
                                             text = "C",
                                             width = 100,
                                             height = 50,
                                             fg_color = "#545454",
                                             command = full_delete
                                             )

potentiate_button = customtkinter.CTkButton(master = window,
                                            text = "^",
                                            width = 100,
                                            height = 50,
                                            fg_color = "#545454",
                                            command = potentiate
                                            )

open_bracket_button = customtkinter.CTkButton(master = window,
                                              text="(",
                                              width = 100,
                                              height = 50,
                                              fg_color = "#545454",
                                              command = open_bracket
                                              )

closing_bracket_button = customtkinter.CTkButton(master = window,
                                                 text=")",
                                                 width = 100,
                                                 height = 50,
                                                 fg_color = "#545454",
                                                 command = close_bracket
                                                 )

del_button = customtkinter.CTkButton(master = window,
                                     text="Del",
                                     width = 100,
                                     height = 50,
                                     fg_color = "#545454",
                                     command = partial_delete
                                     )


#bind function buttons to keyboard buttons

window.bind('<Return>', lambda event: equal())
window.bind('<+>', lambda event: plus())
window.bind('-', lambda event: minus())
window.bind('*', lambda event: multiplicator())
window.bind('/', lambda event: division())
window.bind('%', lambda event: rest())
window.bind('<Delete>', lambda event: full_delete())
window.bind('<BackSpace>', lambda event: partial_delete())
window.bind('(', lambda event: open_bracket())
window.bind(')', lambda event: close_bracket())

#number buttons

number_0 = customtkinter.CTkButton(master = window,
                                   text="0",
                                   width = 100,
                                   height = 50,
                                   fg_color = "#eb711a",
                                   command = n_0
                                   )

number_1 = customtkinter.CTkButton(master = window,
                                   text="1",
                                   width = 100,
                                   height = 50,
                                   fg_color = "#eb711a",
                                   command = n_1
                                   )

number_2 = customtkinter.CTkButton(master = window,
                                   text="2",
                                   width = 100,
                                   height = 50,
                                   fg_color = "#eb711a",
                                   command = n_2
                                   )

number_3 = customtkinter.CTkButton(master = window,
                                   text="3",
                                   width = 100,
                                   height = 50,
                                   fg_color = "#eb711a",
                                   command = n_3
                                   )

number_4 = customtkinter.CTkButton(master = window,
                                   text="4",
                                   width = 100,
                                   height = 50,
                                   fg_color = "#eb711a",
                                   command = n_4
                                   )

number_5 = customtkinter.CTkButton(master = window,
                                   text="5",
                                   width = 100,
                                   height = 50,
                                   fg_color = "#eb711a",
                                   command = n_5
                                   )

number_6 = customtkinter.CTkButton(master = window,
                                   text="6",
                                   width = 100,
                                   height = 50,
                                   fg_color = "#eb711a",
                                   command = n_6
                                   )

number_7 = customtkinter.CTkButton(master = window,
                                   text = "7",
                                   width = 100,
                                   height = 50,
                                   fg_color = "#eb711a",
                                   command = n_7
                                   )

number_8 = customtkinter.CTkButton(master = window,
                                   text = "8",
                                   width = 100,
                                   height = 50,
                                   fg_color = "#eb711a",
                                   command = n_8
                                   )

number_9 = customtkinter.CTkButton(master = window,
                                   text = "9",
                                   width = 100,
                                   height = 50,
                                   fg_color = "#eb711a",
                                   command= n_9
                                   )

#binding of the buttons to the numbpad keys -> 1 to 5 is different for some reason, e.g. '<1>' would be left click on mouse

window.bind('<0>', lambda event: n_0())
window.bind('1', lambda event: n_1())
window.bind('2', lambda event: n_2())
window.bind('3', lambda event: n_3())
window.bind('4', lambda event: n_4())
window.bind('5', lambda event: n_5())
window.bind('<6>', lambda event: n_6())
window.bind('<7>', lambda event: n_7())
window.bind('<8>', lambda event: n_8())
window.bind('<9>', lambda event: n_9())

#define grid

window.columnconfigure((0,1,2,3), weight = 0)
window.rowconfigure((0,1,2,3), weight = 0)

#input field

input_field.grid(row = 0, column = 0, columnspan = 4, padx = (10,0), pady = (10,5), sticky = "nswe")

output_frame.grid(row = 1, column = 0, columnspan = 4, padx = (10,0), pady = (5,10), sticky = "nwe")
output_field.grid(row=1, column = 0, padx = 10, columnspan = 4, pady = 5, sticky = "nswe")

# buttons

number_7.grid(row=2, column=0, sticky = "w", padx = (10,0))
number_8.grid(row=2, column=1, sticky = "w", padx = 0)
number_9.grid(row=2, column=2, sticky = "w", padx = 0)
plus_button.grid(row=2, column=3)
number_4.grid(row=3, column=0,sticky = "w", padx = (10,0))
number_5.grid(row=3, column=1)
number_6.grid(row=3, column=2)
minus_button.grid(row=3, column=3)
number_1.grid(row=4, column=0, sticky = "w", padx = (10,0))
number_2.grid(row=4, column=1)
number_3.grid(row=4, column=2)
multiplicator_button.grid(row=4, column=3)
number_0.grid(row=5, column=0, sticky = "w", padx = (10,0))
open_bracket_button.grid(row=5, column=1)
closing_bracket_button.grid(row=5, column=2)
division_button.grid(row=5, column=3)
rest_button.grid(row=6, column=0, sticky = "w", padx = (10,0))
del_button.grid(row=6, column=1)
full_delete_button.grid(row=6, column=2)
equal_button.grid(row=6, column=3)

window.mainloop()