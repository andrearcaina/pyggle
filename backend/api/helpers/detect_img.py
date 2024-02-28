import cv2
from easyocr import Reader
import numpy as np

image_directory = "C:/Users/dtand/Documents/GitHub/pyggle/backend/data/images/"

images = [cv2.imread(image_directory + f"test{i}.png") for i in range(1, 4)]

reader = Reader(['en'])

results = reader.readtext(images[0])

letters = []

for detection in results:
    text = detection[1].replace('|', '').replace('$', 's').replace('0', 'o').lower()
    letters.append(text)

print(letters)

# the images need to be preprocessed for further optimization and better results of the letters
# follow: https://www.youtube.com/watch?v=ADV-AjAXHdc