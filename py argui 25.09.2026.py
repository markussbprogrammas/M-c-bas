import PySimpleGUI as sg
from PIL import Image
def bilde():
 datne = values["-FILE-"]
 with Image.open(datne)as im:
    print(datne, im.format, f"{im.size}x{im.mode}")
    izmers = (100, 100)
    im.thumbnail(izmers)
    im.save("bilde-maza.png", im.format)
    window["-IMAGE-"].update(filename="bilde-maza.png")


layout = [[sg.Input(key="-FILE-"),sg.FileBrowse("Pārlūkot")],
[sg.Button("Parādīt"), sg.Button("Iziet")], [sg.Image(filename="bilde.png",key="-IMAGE-")]]

window = sg.Window("Bilde", layout)

while True:
    event,values = window.read()

    if event == sg.WIN_CLOSED or event == "Iziet":
        break

    if event == "Parādīt":
        bilde()
        
window.close()