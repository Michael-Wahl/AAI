import PySimpleGUI as sg
from PIL import Image
import io
import json
import random
import os

#loading json file
with open('output/mapping.json', 'r') as file:
    obj = json.load(file)

print(obj)


file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]

emo_dic = {'-ANGRY-': 'angry', '-DISGUST-': 'disgust', '-FEAR-': 'fear', '-HAPPY-': 'happy', '-NEUTRAL-': 'neutral','-SAD-':'sad', '-SURPRISED-': 'surprised'}

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



def random_image():
    input_path = os.getcwd() + '\input'
    image_file = random.choice(os.listdir(input_path))
    # image_path = sg.popup_get_file('Open', no_window=True)
    image = Image.open(input_path + '\\' + image_file)

    #image size
    image.thumbnail((400, 400))

    # handling different formats than PNG
    bio = io.BytesIO()
    # Actually store the image in memory in binary
    image.save(bio, format="PNG")

    return bio.getvalue(), image_file

def check_emotion(image_file, event):
    emo_label = obj[image_file][0]['emo_label']
    if emo_label == emo_dic[event]:
        return True
    return False



def emotionmode_f():
    shown_images = []
    image, image_name = random_image()
    shown_images.append(image_name)

    emotion_col = sg.Column([
        [sg.Button('wütend', key='-ANGRY-'), sg.Button('ekelerfüllt', key='-DISGUST-'), sg.Button('ängstlich', key='-FEAR-')],
        [sg.Button('glücklich', key='-HAPPY-'), sg.Button('neutral', key='-NEUTRAL-')],
        [sg.Button('traurig', key='-SAD-'), sg.Button('überrascht', key='-SURPRISED-')],
    ])

    image_col = sg.Column([[sg.Image(image, key = '-IMAGE-')]])
    emotion_lay = [[sg.Text("Welche Emotion wird hier gezegt?")],
                   [emotion_col, image_col],
                   [sg.Text(visible = False, enable_events=True, key = '-VALID-'), sg.Button('Nächstes', key = '-NEXT-') ,sg.Button('Beenden', key = '-QUIT-')]]

    #original = Image.open(image_path)
    emotionmode_win = sg.Window('Emotionszuordnung', emotion_lay)


    while True:
        event, values = emotionmode_win.read(timeout = 50)
        #todo: function to load picture
        if event in (None, '-QUIT-'):
            break
        elif event in ('-ANGRY-','-DISGUST-','-FEAR-','-HAPPY-','-NEUTRAL-','-SAD-','-SURPRISED-'):
            if check_emotion(image_name,event):
                emotionmode_win['-VALID-'].update(visible=True)
                emotionmode_win['-VALID-'].update('Richtig')
            else:
                emotionmode_win['-VALID-'].update(visible=True)
                emotionmode_win['-VALID-'].update('Falsch')
        elif event == '-NEXT-':
            emotionmode_win['-VALID-'].update(visible=False)

            #todo: print that all images where seen
            while image_name in shown_images:
                image, image_name = random_image()

            emotionmode_win['-IMAGE-'].update(image)
            shown_images.append(image_name)



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


#todo: Köpfe ausschneiden, wie mit Gruppenbilder umgehen?