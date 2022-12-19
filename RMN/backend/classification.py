from rmn import RMN
import cv2
from PIL import Image

m = RMN()

def classify_image(image_file):
    image = cv2.imread(image_file)
    result = m.detect_emotion_for_single_frame(image)
    return result
