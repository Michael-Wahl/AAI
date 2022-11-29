import PySimpleGUI as sg
from PIL import Image
import io

file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]

# functions handling windows

def gamemodes_f():
    gamemodes_lay = [[sg.Text("Welchen Spielmodi?")],
                     [sg.Button('Emotionsbestimmung', key='-EMOTIONMODE-'), sg.Button('Hintergrund', key='-BACKGROUNDMODE-')],
                     [sg.Text(size=(40, 1), key='-OUTPUT-')],
                     [sg.Button('Ok'), sg.Button('Quit')]]

    gamemodes_win = sg.Window('Spielmodi', gamemodes_lay)

    while True:
        event, values = gamemodes_win.read()
        if event in (None, 'Quit'):
            break
        elif event == '-EMOTIONMODE-':
            emotionmode_f()
        elif event == '-BACKGROUNDMODE-':
            backgroundmode_f()

    gamemodes_win.close()

def emotionmode_f():

    image_path = sg.popup_get_file('Open', no_window=True)
    image = Image.open(image_path)

    #handling different formats than PNG
    bio = io.BytesIO()
    # Actually store the image in memory in binary
    image.save(bio, format="PNG")

    data = bio.getvalue()


    emotion_col = sg.Column([
        [sg.Button('wütend', key='-ANGRY-'), sg.Button('ekelerfüllt', key='-DISGUST-'), sg.Button('ängstlich', key='-FEAR-')],
        [sg.Button('glücklich', key='-HAPPY-'), sg.Button('neutral', key='-NEUTRAL-')],
        [sg.Button('traurig', key='-SAD-'), sg.Button('überrascht', key='-SURPRISED-')],
    ])

    image_col = sg.Column([[sg.Image(data, key = '-IMAGE-')]])
    emotion_lay = [[sg.Text("Welche Emotion wird hier gezegt?")],
                   [emotion_col, image_col],
                   [sg.Button('Ok'), sg.Button('Quit')]]

    original = Image.open(image_path)
    emotionmode_win = sg.Window('Emotionszuordnung', emotion_lay)

    while True:
        event, values = emotionmode_win.read(timeout = 50)
        if event in (None, 'Quit'):
            break

    emotionmode_win.close()

def backgroundmode_f():
    background_lay = [[sg.Text("Stimmen Emotion und Hintergrund überein?")],
                      [sg.Button('Ja', key='-YES-'), sg.Button('Nein', key='-NO-')],
                      [sg.Button('Ok'), sg.Button('Quit')]]

    backgroundmode_win = sg.Window('Hintergrundspielmodus', background_lay)

    while True:
        event, values = backgroundmode_win.read()
        if event in (None, 'Quit'):
            break

    backgroundmode_win.close()



#setup welcome window

welcome_lay = [[sg.Text("Wie heißt du?")],
               [sg.Input(key='-INPUT-')],
               [sg.Text(size=(40, 1), key='-OUTPUT-')],
               [sg.Button('Ok'), sg.Button('Akzeptieren', key='-ACCEPT-'), sg.Button('Quit')]]


# Create the window
welc_win = sg.Window('Window Title', welcome_lay)

# Display and interact with the Window using an Event Loop
while True:
    event, values = welc_win.read()
    # See if user wants to quit or window was closed
    if event in (None, 'Quit'):
        break

    welc_win['-OUTPUT-'].update('Hallo ' + values['-INPUT-'] + "! Willkommen zu Emotionen spielend lernen")
    if event == '-ACCEPT-':
        welc_win.close()
        gamemodes_f()

# Finish up by removing from the screen
welc_win.close()
