import io
import json
import ntpath
import os
import random
import tkinter.filedialog
from os.path import isfile

import PySimpleGUI as sg
from PIL import Image
from threading import Thread

# loading json file
with open('output/mapping.json', 'r') as file:
    obj = json.load(file)

print(obj)

file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]

emo_dic = {'-ANGRY-': 'angry', '-DISGUST-': 'disgust', '-FEAR-': 'fear', '-HAPPY-': 'happy', '-NEUTRAL-': 'neutral',
           '-SAD-': 'sad', '-SURPRISED-': 'surprised'}


# functions handling windows

def gamemodes_f():
    gamemodes_lay = [[sg.Text("Welchen Spielmodi?")],
                     [sg.Button('Emotionsbestimmung', key='-EMOTIONMODE-'),
                      sg.Button('Hintergrund', key='-BACKGROUNDMODE-')],
                     [sg.Text(size=(40, 1), key='-OUTPUT-')],
                     [sg.Button('Ok'), sg.Button('Beenden', key='-QUIT-')]]

    gamemodes_win = sg.Window('Spielmodi', gamemodes_lay)

    while True:
        event, values = gamemodes_win.read()
        if event in (None, '-QUIT-'):
            break
        elif event == '-EMOTIONMODE-':
            emotionmode_f()
        elif event == '-BACKGROUNDMODE-':
            backgroundmode_f()

    gamemodes_win.close()


def random_image():
    input_path = os.getcwd() + '\\faces'
    image_file = random.choice(os.listdir(input_path))
    # image_path = sg.popup_get_file('Open', no_window=True)
    image = Image.open(input_path + '\\' + image_file)

    # image size
    image.thumbnail((600, 600))

    # handling different formats than PNG
    bio = io.BytesIO()
    # Actually store the image in memory in binary
    image.save(bio, format="PNG")

    return bio.getvalue(), image_file


def check_emotion(image_file, event):
    i = int(image_file[0])
    original_im = image_file[2:]

    emo_label = obj[original_im][i]['emo_label']
    if emo_label == emo_dic[event]:
        return True
    return False


def emotionmode_f():
    shown_images = []
    image, image_name = random_image()
    shown_images.append(image_name)

    emotion_col = sg.Column([
        [sg.Button('wütend', key='-ANGRY-'), sg.Button('ekelerfüllt', key='-DISGUST-'),
         sg.Button('ängstlich', key='-FEAR-')],
        [sg.Button('glücklich', key='-HAPPY-'), sg.Button('neutral', key='-NEUTRAL-')],
        [sg.Button('traurig', key='-SAD-'), sg.Button('überrascht', key='-SURPRISED-')],
    ])

    image_col = sg.Column([[sg.Image(image, key='-IMAGE-')]])
    emotion_lay = [[sg.Text("Welche Emotion wird hier gezegt?")],
                   [emotion_col, image_col],
                   [sg.Text(visible=False, enable_events=True, key='-VALID-'), sg.Button('Nächstes', key='-NEXT-'),
                    sg.Button('Beenden', key='-QUIT-')]]

    emotionmode_win = sg.Window('Emotionszuordnung', emotion_lay)

    while True:
        event, values = emotionmode_win.read(timeout=50)

        if event in (None, '-QUIT-'):
            break
        elif event in ('-ANGRY-', '-DISGUST-', '-FEAR-', '-HAPPY-', '-NEUTRAL-', '-SAD-', '-SURPRISED-'):
            if check_emotion(image_name, event):
                emotionmode_win['-VALID-'].update(visible=True)
                emotionmode_win['-VALID-'].update('Richtig')
            else:
                emotionmode_win['-VALID-'].update(visible=True)
                emotionmode_win['-VALID-'].update('Falsch')
        elif event == '-NEXT-':
            emotionmode_win['-VALID-'].update(visible=False)

            # todo: print that all images where seen
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


def start_window():
    # setup welcome window

    welcome_lay = [[sg.Text("Wie heißt du?")],
                   [sg.Input(key='-INPUT-')],
                   [sg.Text(size=(40, 1), key='-OUTPUT-')],
                   [sg.Button('Ok'), sg.Button('Akzeptieren', key='-ACCEPT-'), sg.Button('Beenden', key='-QUIT-')]]

    # Create the window
    welc_win = sg.Window('Window Title', welcome_lay)

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = welc_win.read()
        # See if user wants to quit or window was closed
        if event in (None, '-QUIT-'):
            break

        welc_win['-OUTPUT-'].update('Hallo ' + values['-INPUT-'] + "! Willkommen zu Emotionen spielend lernen")
        if event == '-ACCEPT-':
            welc_win.close()
            # upload_images()
            webcam_f()
            # gamemodes_f()

    # Finish up by removing from the screen
    welc_win.close()

def webcam_f():
    webcam_lay = [[sg.Text("Welche Emotion")],
                  [sg.Button('Glücklich', key='-HAPPY-'), sg.Button('Nein', key='-NO-')],
                  [sg.Button('Next', key='-NEXT-')]
                  ]
    webcam_win = sg.Window('Webcammodus', webcam_lay, size=(500, 500))

    while True:
        event, values = webcam_win.read()
        if event in (None, 'Quit'):
            break
        if event == "-HAPPY-":
            getWebcamPics("happy")
        if event == "-NEXT-":
            upload_images()

def upload_images():
    upload_lay = [[sg.Text("Bitte Bilder hochladen")],
                  [sg.Button('Ja', key='-YES-'), sg.Button('Nein', key='-NO-')],
                  [sg.Button('Next', key='-NEXT-')]
                  ]
    upload_win = sg.Window('Bilderverwaltung', upload_lay, size=(500, 500))

    while True:
        event, values = upload_win.read()
        if event in (None, 'Quit'):
            break
        if event == "-YES-":
            files = tkinter.filedialog.askopenfilename()
            save_file_names(files)
            # upload_win.refresh() todo: update window after changing layout by adding loaded images
            print(files)

        # after uploading images -> emotion detection with ai
        if event == "-NEXT-":
            thread = Thread(target=execute_face_emotion_detection_ai())
            thread.start()
            upload_win.close()
            thread.join()
            gamemodes_f()  # then change to game modi



def execute_face_emotion_detection_ai(): # todo: debug classification ai is very time-consuming
    import classification
    exec("classification")


def save_file_names(image_name):
    if not isfile("filenames.txt"): # create a file to save image's paths if it does not exist.
        f = open("filenames.txt", "w")
    file_name = "filenames.txt"
    if isfile(file_name):
        with open(file_name, "r", encoding="utf-8") as f1: # file is closed automatically after reading
            text = f1.readlines()
            print(text)
            if image_name + "\n" not in text:  # todo: handle allowed file types png or jpeg, images with human faces
                with open(file_name, "a", encoding="utf-8") as f:
                    f.write(image_name)
                    f.write("\n")
                    print("OK")  # todo: display status load images ok gui
                    save_images_in_input(file_name)
            else:  # todo: handle error window gui
                print("Datei ist bereits vorhanden. Bitte versuchen Sie nochmal.")




def save_images_in_input(file):
    with open(file, "r", encoding="utf-8") as f:
        filenames = f.readlines()
        for name in filenames: # todo: inhalt von filenames.txt sollte gelöscht werden after each spiel
            processed_name = remove_new_line(name)
            print(processed_name)
            filename = ntpath.basename(processed_name)  # todo: display file names in layout window
            print(filename)
            image_path = os.getcwd() + '\\input'
            image = Image.open(processed_name)
            image.save(f"{image_path}\\{filename}", "PNG")  # todo: debug file saving slow
    # layout.append([processed_name])


"""
Remove separator new line from each path to images.
"""


def remove_new_line(name):
    name1 = name.replace("\n", "")
    return name1


"""
Start the app here.
"""

if __name__ == "__main__":
    start_window()

# todo: Köpfe ausschneiden (Max)
# todo: Bilder selbst hochladen + Adminfenster (Van)
# Webcam (Michael)
# todo: Hintergründe Spielmodus (Lydia)
