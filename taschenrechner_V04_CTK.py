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

window.mainloop()