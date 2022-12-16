from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import base64
import uuid

from classification import classify_image

app = Flask(__name__)
CORS(app)

unclassified = []
classified = {}

# For uploading webcam pictures as json, stores them in images folder, filename gets added to unclassified array
@app.route('/image-upload', methods=['POST'])
def save_image():
    # Check if the request is JSON and has the 'image' key
    if request.is_json and 'image' in request.get_json():
        # Decode the image data and save it to a file
        image_data = request.get_json()['image']
        image_data = image_data[image_data.index(',') + 1:]
        image_data = base64.b64decode(image_data)

        # Create a subfolder in the directory to store the images
        subfolder = 'images'
        if not os.path.exists(subfolder):
            os.makedirs(subfolder)
        
        # Saving the image with a unique id as filename
        filename = f'{uuid.uuid4()}.jpg'
        filepath = os.path.join(subfolder, filename)
        
        with open(filepath, 'wb') as f:
            f.write(image_data)
            unclassified.append(filename)
        return f'{filename}', 200
    else:
        return 'Invalid request', 400

# Classify all unclassified images files in unclassified array, save results in classified dict.
@app.route('/classify', methods=['GET'])
def classify():
    if not unclassified:
        return 'No filenames provided', 400
  
    for filename in unclassified:
        filepath = os.path.join('images', filename)
        if not os.path.exists(filepath):
            return f'File "{filepath}" does not exist', 404
    
        with open(filepath, 'r') as file:
            # Perform operation on the file
            result = classify_image(filepath)
            classified[filename] = result
            print(classified)
    
    return classified, 200


