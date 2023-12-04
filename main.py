import PySimpleGUI as sg
from math import sqrt

visor = ""
btn_num = []
btn_sinais=  []


# BUTTON CREATOR
def button(title: str, special=False):
    if title.isnumeric():
        btn_num.append(title)
    elif special == True:
        pass
    else:
        btn_sinais.append(title)

    return sg.Button(button_text=(title), size=(4, 2), button_color="#fc6f38", font=("Calibri 15"))

layout = [
    [sg.Text(visor, key="v", size=(100, 2), font=("Calibri 18"), background_color="White", text_color="Black") ],
    [],
    [button("C", True), button("AC", True), button("("), button(")"), button("√", True)],
    [button("7"), button("8"), button("9"), button("/"), button("x²", True)],
    [button("4"), button("5"), button("6"), button("*"), button("^", True)],
    [button("1"), button("2"), button("3"), button("-"), button("=", True)],
    [button("0"), button("."), button("π", True), button("+")],
    [sg.Text("", key="alert", background_color="Black", text_color="Red", font=("Calibri 12"), size=(15, 3))]

]

sg.theme('reddit')
window = sg.Window(title='Calculator', layout=layout, background_color="Black")

while True:
    event, values = window.read()
    # WIN CLOSE
    if event == sg.WIN_CLOSED:
        break
    # NUMS BUTTONS
    for btn in btn_num:
        if event == btn:
            visor = visor + btn
            window["v"].update(visor)
    
    # ARITHMETIC OPERATORS
    for btn in btn_sinais:
        if event == btn:
            visor = visor + btn
            window["v"].update(visor)
    
    # SOME FUCTIONS
    if event == "C":
        visor = visor[:-1]
        window["v"].update(visor)
    
    if event == "AC":
        visor = ""
        window["v"].update(visor)
    
    if event == "√":
        coman = "sqrt("
        visor = visor + coman
        window["v"].update(visor)
    
    if event == "x²":
        visor = visor + "**2"
        window["v"].update(visor)
    
    if event == "^":
        visor = visor + "**"
        window["v"].update(visor)
    
    if event == "π":
        visor = visor + "3.14"
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
    
window.close()
