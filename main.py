import PySimpleGUI as sg
from math import sqrt

visor = ""

def button(title, x, y):
    return sg.Button(button_text=(title), size=(x, y), button_color="#fc6f38", font=("Calibri 15"))

layout = [
    [sg.Input(default_text=visor, key="v", size=(400, 2), font=("Calibri 18"), background_color="White", text_color="Black") ],
    [],
    [button("C", 3, 2), button("AC", 3, 2), button("(", 3, 2), button(")", 3, 2), button("√", 3, 2)],
    [button("7", 3, 2), button("8", 3, 2), button("9", 3, 2), button("/", 3, 2), button("x²", 3, 2)],
    [button("4", 3, 2), button("5", 3, 2), button("6", 3, 2), button("*", 3, 2), button("^", 3, 2)],
    [button("1", 3, 2), button("2", 3, 2), button("3", 3, 2), button("-", 3, 2), button("=", 3, 2,)],
    [button("0", 3, 2), button(".", 3, 2), button("π", 3, 2), button("+", 3, 2)],
    [sg.Text("", key="alert", background_color="Black", text_color="Red", font=("Calibri 12"))]

]

sg.theme('reddit')
window = sg.Window("Calculadora", layout, size=(415, 450), background_color="#000000")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "C":
        visor = visor[:-1]
        window["v"].update(visor)
    if event == "AC":
        visor = ""
        window["v"].update(visor)
    if event == "(":
        visor = visor + "("
        window["v"].update(visor)
    if event == ")":
        visor = visor + ")"
        window["v"].update(visor)
    if event == "√":
        coman = "sqrt("
        visor = visor + coman
        window["v"].update(visor)
    if event == "7":
        visor = visor + "7"
        window["v"].update(visor)
    if event == "8":
        visor = visor + "8"
        window["v"].update(visor)
    if event == "9":
        visor = visor + "9"
        window["v"].update(visor)
    if event == "/":
        visor = visor + "/"
        window["v"].update(visor)
    if event == "x²":
        visor = visor + "**2"
        window["v"].update(visor)
    if event == "4":
        visor = visor + "4"
        window["v"].update(visor)
    if event == "5":
        visor = visor + "5"
        window["v"].update(visor)
    if event == "6":
        visor = visor + "6"
        window["v"].update(visor)
    if event == "*":
        visor = visor + "*"
        window["v"].update(visor)
    if event == "^":
        visor = visor + "**"
        window["v"].update(visor)
    if event == "1":
        visor = visor + "1"
        window["v"].update(visor)
    if event == "2":
        visor = visor + "2"
        window["v"].update(visor)
    if event == "3":
        visor = visor + "3"
        window["v"].update(visor)
    if event == "-":
        visor = visor + "-"
        window["v"].update(visor)
    if event == "=":
        try:
            r = eval(visor)
            visor = str(r)
            window["v"].update(visor)
        except SyntaxError:
            window["alert"].update("Operação Inválida")
        else:
            window["alert"].update("")
    if event == "0":
        visor = visor + "0"
        window["v"].update(visor)
    if event == ".":
        visor = visor + "."
        window["v"].update(visor)
    if event == "π":
        visor = visor + "3.14"
        window["v"].update(visor)
    if event == "+":
        visor = visor + "+"
        window["v"].update(visor)
window.close()
