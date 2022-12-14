from flask import Flask, request, send_file
from flask_cors import CORS
import os
import base64
import uuid

from classification import classify_image

app = Flask(__name__)
CORS(app)

# Imagefilename with the result of the classification.
classified = {}

# For uploading webcam pictures as json, stores them in images folder and classifies emotion in dict
@app.route('/image-upload', methods=['POST'])
def save_image():
    # Check if the request is JSON and has the 'image' key
    if request.is_json and 'image' in request.get_json():
        # Decode the image data and save it to a file
        image_data = request.get_json()['image']
        image_data = image_data[image_data.index(',') + 1:]
        image_data = base64.b64decode(image_data)

        target = request.get_json()['target']
        print(target)

        # Create a subfolder in the directory to store the images
        subfolder = 'images'
        if not os.path.exists(subfolder):
            os.makedirs(subfolder)
        
        # Saving the image with a unique id as filename
        filename = f'{uuid.uuid4()}.jpg'
        filepath = os.path.join(subfolder, filename)
        
        with open(filepath, 'wb') as f:
            f.write(image_data)

        # Classify emotion and save to dict
        with open(filepath, 'r') as file:
            result = classify_image(filepath)
            classified[filename] = result
            print(result[0].get('emo_label'))

            # Check if emotion matches
            if result[0].get('emo_label') == target:
                if result[0].get('emo_proba') > 0.93:
                    return "Target matched", 200

        # if emotion does not match target or proba to low, delete image file and dict entry
        del classified[filename]
        os.remove(filepath)
        return 'Target not matched', 200
        
    else:
        return 'Invalid request', 400

# # Classify all unclassified images files in unclassified array, save results in classified dict.
# @app.route('/classify', methods=['GET'])
# def classify():
#     if not unclassified:
#         return 'No filenames provided', 400
  
#     for filename in unclassified:
#         filepath = os.path.join('images', filename)
#         if not os.path.exists(filepath):
#             return f'File "{filepath}" does not exist', 404
    
#         with open(filepath, 'r') as file:
#             # Detect emotion, append result to dict
#             result = classify_image(filepath)
#             classified[filename] = result
#             unclassified.remove(filename)
#             print(classified)
    
#     return classified, 200

# Returns the filenames of all classified images.
@app.route('/getAllImages', methods=['GET'])
def list_files():
    i = list(classified.keys())
    return (i)

# Getting specifc image file based on filename
@app.route('/getImage/<image_name>')
def get_image(image_name):
    if not image_name == 'undefined':
        image_path = os.path.join('images', image_name)
        return send_file(image_path, mimetype='image/jpeg')
    return 'File not found', 404

# Getting specifc image file based on filename
@app.route('/getAllEmotions')
def get_emotions():
    return classified, 200

@app.route('/getEmotion/<image_name>')
def get_emotion(image_name):
    if not image_name == 'undefined':
        if image_name in classified:
            return classified[image_name], 200
    return "Classification for image_name not found", 404


"""
Upload images from users on the server and return the paths of uploaded images.
"""
app.config["UPLOAD_FOLDER"] = "uploads" # define an upload folder
app.config["ALLOWED_EXTENSIONS"] = ["jpg", "jpeg", "png"] # allowed file extensions

def allowed_file(filename):
    # Check if the file extension is in the ALLOWED_EXTENSIONS list.
    return "." in filename and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

    # TODO debug needed
@app.route("/upload-image", methods=["POST"])
def upload():
    if "image" not in request.files:
        return jsonify({"error": "No file found"}), 400

    file = request.files["image"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": f"File type not allowed. Allowed types: {app.config['ALLOWED_EXTENSIONS']}"}), 400
    #check if the upload folder exists, if not create it.
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])
    #save the file to the filesystem
    file.save(f'{app.config["UPLOAD_FOLDER"]}/{file.filename}')
    path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    return jsonify({"image_path": path})

