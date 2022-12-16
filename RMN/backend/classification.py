# libraries required to run
#pip install rmn
#pip install opencv-python

from rmn import RMN
import cv2
from PIL import Image


m = RMN()

# Storing the image names and the results of the classification
#results = {}

def classify_image(image_file):
    image = cv2.imread(image_file)
    result = m.detect_emotion_for_single_frame(image)
    return result





# with open('output/mapping.json', 'r') as file:
#     map_file = json.load(file)

# for im in map_file:
#      facelst = map_file[im]
#      image = Image.open(input_path+'/'+im)
#      i = 0

#      #cutting out each face in picture

#      for face in facelst:
#          face_dic = facelst[i]
#          face_im = image.crop((face_dic['xmin'],face_dic['ymin'],face_dic['xmax'],face_dic['ymax']))
#          face_im.save(facefolder + '\\' + str(i) + '_' + im)
#          i+=1


