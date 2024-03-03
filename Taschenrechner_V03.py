# ToDo: GUI erstellen

import tkinter as tk

window = tk.Tk()

title = tk.Label(text="Welcome to my calculator! Let the math begin. ",
                 width = 40,
                 height = 15)

equal_button = tk.Button(
    text="+",
)


title.pack()


window.mainloop()

"""
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