# libraries required to run
#pip install rmn
#pip install opencv-python

import os
from rmn import RMN
import cv2
import json
from PIL import Image

# input and output directories
dirname = os.path.dirname(__file__)
inputfolder = os.path.join(dirname, 'input')
outputfolder = os.path.join(dirname, 'output')
facefolder = os.path.join(dirname, 'faces')

input_path = os.getcwd() + '\input'

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

#loading file to cut out faces

with open('output/mapping.json', 'r') as file:
    map_file = json.load(file)

for im in map_file:
     facelst = map_file[im]
     image = Image.open(input_path+'/'+im)
     i = 0

     #cutting out each face in picture

     for face in facelst:
         face_dic = facelst[i]
         face_im = image.crop((face_dic['xmin'],face_dic['ymin'],face_dic['xmax'],face_dic['ymax']))
         face_im.save(facefolder+'/'+str(i)+'_'+im)
         i+=1


