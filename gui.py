import PySimpleGUI as sg


def window():
    layout = [
        [sg.Text('Выберите папку'), sg.InputText(), sg.FolderBrowse("Выбрать папку")],
        [sg.Submit("Применить")],
        ]
    sg.theme('LightGrey')
    window = sg.Window('Давайте что-нибудь отсортируем', layout)

    while True:
            event, values = window.read()
            print(values)
            if(values['Выбрать папку'] != ""):
                return values['Выбрать папку']
            if(event in ('Exit', 'Cancel', None)):
                break
