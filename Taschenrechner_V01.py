# Hier soll erst ein Taschenrechner, dann ein "Advanced" Taschenrechner mit
# Zusatzfunktionen entstehen

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