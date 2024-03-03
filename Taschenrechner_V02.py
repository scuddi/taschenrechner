# ToDo: Add functions to V01

input_zahl_1 = input("Geben Sie die erste Zahl ein: ")
input_operation = input("Welche Operation möchten Sie vornehmen? Möglich sind: +, -, *, / und Rest: ")
input_zahl_2 = input("Geben Sie die zweite Zahl ein: ")

# Alle Funktionen für Mathe-Operationen

def add(input_zahl_1, input_zahl_2):
    return float(input_zahl_1) + float(input_zahl_2)

def subtract(input_zahl_1, input_zahl_2):
    return float(input_zahl_1) - float(input_zahl_2)

def mulitply(input_zahl_1, input_zahl_2):
    return float(input_zahl_1) * float(input_zahl_2)

def divide(input_zahl_1, input_zahl_2):
    return float(input_zahl_1) / float(input_zahl_2)

def rest(input_zahl_1, input_zahl_2):
    return float(input_zahl_1) % float(input_zahl_2)

# Wann wird welche Funktion aufgerufen?

if input_operation == "+":
    result = add(input_zahl_1, input_zahl_2)

elif input_operation == "-":
    result = subtract(input_zahl_1, input_zahl_2)

elif input_operation == "*":
    result = mulitply(input_zahl_1, input_zahl_2)

elif input_operation == "/":
    result = divide(input_zahl_1, input_zahl_2)

elif input_operation == "Rest":
    result = rest(input_zahl_1, input_zahl_2)

else:
    print("Diese Operation ist nicht bekannt, probieren Sie +, -, *, / oder %.")

print("Das Ergebnis ist", result)