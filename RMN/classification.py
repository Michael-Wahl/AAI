# libraries required to run
#pip install rmn
#pip install opencv-python

import os
from rmn import RMN
import cv2
import json

# input and output directories
dirname = os.path.dirname(__file__)
inputfolder = os.path.join(dirname, 'input')
outputfolder = os.path.join(dirname, 'output')

m = RMN()

# Storing the image names and the results of the classification
results_mapping = {}

# setting up loop to batch classifiy all images in input folder, saving to output folder
for filename in os.listdir(inputfolder):
    print (filename)

    # Reading image and face + emotion detection
    image = cv2.imread(f"{inputfolder}/{filename}")
    results = m.detect_emotion_for_single_frame(image)
    print(results)

    # Adding boxes and saving to new file
    image = m.draw(image, results)
    cv2.imwrite(f"{outputfolder}/output_{filename}", image)

    # Appending results data
    results_mapping[filename] = results

# Saving results mapping as json in output folder
print(results_mapping)
with open(f'{outputfolder}/mapping.json', 'w') as file:
    json.dump(results_mapping, file, indent=4)
