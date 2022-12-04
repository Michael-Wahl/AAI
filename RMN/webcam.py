import os
from rmn import RMN
import cv2
from PIL import Image
import numpy as np
import json
import uuid

# output directory
dirname = os.path.dirname(__file__)
outputfolder = os.path.join(dirname, 'output')

m = RMN()

# Using webcam
vid = cv2.VideoCapture(0)

# Starts webcam and saves images when emotion given in parameter matches
def getWebcamPics(emo_label_target):
    x = 0
    # For new detectionresults
    resultsmapping = {}
    IDImage = 0

    while True:
        # Getting every frame from webcam
        ret, frame = vid.read()
        cv2.imshow('frame', frame)

        if frame is None or ret is not True:
            continue

        # Detecting emotion for each frame
        npframe = np.fliplr(frame).astype(np.uint8)
        results = m.detect_emotion_for_single_frame(npframe)

        if results:
            emo_proba = results[0].get('emo_proba')
            emo_label = results[0].get('emo_label')

            if emo_proba > 0.97 and emo_label == emo_label_target:
                # Generating random UUID as imagename and saving image as .png
                IDImage = uuid.uuid4().hex
                cv2.imwrite(f'webcam{IDImage}.png', frame)
                
                x = x+1

                # Appending mapping.json file with new data from detected emotion
                with open(f'{outputfolder}/mapping.json') as mappingfile:
                    mappingdata = json.load(mappingfile)

                resultsmapping[f'webcam{IDImage}.png'] = results
                mappingdata.update(resultsmapping)

                with open(f'{outputfolder}/mapping.json', 'w') as newfile:
                    json.dump(mappingdata, newfile, indent=4)

        # For now, stop after 3 images with emotion detected
        if x > 3:
            break
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()

# For testing, uncomment next line
#getWebcamPics('happy')
