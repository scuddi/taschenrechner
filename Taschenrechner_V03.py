# ToDo: GUI erstellen

# ToDo: Ideen:
# ToDo: 1. Anstelle von Entry und Output in der GUI sonst in der Konsole?

import tkinter as tk

#functions for the buttons of the

def plus():
    print("+")

window = tk.Tk()

title = tk.Label(text="Welcome to my calculator!\n\nLet the math begin. ",
                 background = "#bdc7be",
                 foreground = "#111211",
                 width = 37,
                 height = 5
                 )

#input field

input_field = tk.Entry(width = 8 ,
                       font = ("Arial", 20))

#output field

output = "Ergebnis"
output_field = tk.Label(text = output,
                        font = ("bold")
                        )

#operator buttons

equal_button = tk.Button(text="=",
                         width = "8",
                         height = "3",
                         background = "#bdc7be"
                         )

plus_button = tk.Button(text="+",
                        width = "8",
                        height = "3",
                        background = "#bdc7be",
                        command = plus
                        )

minus_button = tk.Button(text="-",
                      width = "8",
                      height = "3",
                      background = "#bdc7be"
                      )

multiplicator_button = tk.Button(text="*",
                         width = "8",
                         height = "3",
                         background = "#bdc7be"
                         )

division_button = tk.Button(text="/",
                         width = "8",
                         height = "3",
                         background = "#bdc7be"
                         )

rest_button = tk.Button(text="Rest",
                        width = "8",
                        height = "3",
                        background = "#bdc7be"
                        )
delete_button = tk.Button(text="C",
                          width = "8",
                          height = "3",
                          background = "#bdc7be"
                          )

#number buttons

number_0 = tk.Button(text="0",
                     width = "8",
                     height = "3",
                     background = "#bdc7be"
                     )

number_1 = tk.Button(text="1",
                     width = "8",
                     height = "3",
                     background = "#bdc7be"
                     )

number_2 = tk.Button(text="2",
                     width = "8",
                     height = "3",
                     background = "#bdc7be"
                     )

number_3 = tk.Button(text="3",
                     width = "8",
                     height = "3",
                     background = "#bdc7be"
                     )

number_4 = tk.Button(text="4",
                     width = "8",
                     height = "3",
                     background = "#bdc7be"
                     )

number_5 = tk.Button(text="5",
                     width = "8",
                     height = "3",
                     background = "#bdc7be"
                     )

number_6 = tk.Button(text="6",
                     width = "8",
                     height = "3",
                     background = "#bdc7be"
                     )

number_7 = tk.Button(text="7",
                     width = "8",
                     height = "3",
                     background = "#bdc7be"
                     )

number_8 = tk.Button(text="8",
                     width = "8",
                     height = "3",
                     background = "#bdc7be"
                     )

number_9 = tk.Button(text="9",
                     width = "8",
                     height = "3",
                     background = "#bdc7be"
                     )

#graphical interface/grid of buttons

title.grid(row=0, column=0, columnspan=4)

#input field

input_field.grid(row=1, column=0, columnspan=2)

#output field

output_field.grid(row=1, column=2, columnspan=2)
#buttons

number_7.grid(row=2, column=0)
number_8.grid(row=2, column=1)
number_9.grid(row=2, column=2)
plus_button.grid(row=2, column=3)
number_4.grid(row=3, column=0)
number_5.grid(row=3, column=1)
number_6.grid(row=3, column=2)
minus_button.grid(row=3, column=3)
number_1.grid(row=4, column=0)
number_2.grid(row=4, column=1)
number_3.grid(row=4, column=2)
multiplicator_button.grid(row=4, column=3)
division_button.grid(row=5, column=0)
rest_button.grid(row=5, column=1)
delete_button.grid(row=5, column=2)
equal_button.grid(row=5, column=3)




window.mainloop()


""" DAS IST VO1, DRAUF ACHTEN!!
input_zahl_1 = input("Geben Sie die erste Zahl ein: ")
input_operation = input("Welche Operation möchten Sie vornehmen? Möglich sind: +, -, *, / und Rest: ")
input_zahl_2 = input("Geben Sie die zweite Zahl ein: ")


if input_operation == "+":
    result = int(input_zahl_1) + int(input_zahl_2)

elif input_operation == "-":
    result = int(input_zahl_1) - int(input_zahl_2)

elif input_operation == "*":
    result = int(input_zahl_1) * int(input_zahl_2)

elif input_operation == "/":
    result = int(input_zahl_1) / int(input_zahl_2)

elif input_operation == "Rest":
    result = int(input_zahl_1) % int(input_zahl_2)

else:
    print("Diese Operation ist nicht bekannt, probieren Sie +, -, *, / oder %.")

print("Das Ergebnis ist", result)

"""