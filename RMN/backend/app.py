from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import base64
import uuid

app = Flask(__name__)
CORS(app)

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
        return f'{filename}', 200
    else:
        return 'Invalid request', 400
