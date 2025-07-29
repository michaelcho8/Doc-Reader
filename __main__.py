import cv2
from PIL import Image

# Convert jpg to png
from ocr.preprocess import convert_to_png
image_path = convert_to_png("home/mccs/Documents/git/Doc-Reader/images/handwritten test.jpg")

# using OpenCV for image display
image = cv2.imread(image_path)
cv2.imshow('Image', image)
cv2.waitkey(0)
cv2.destroyAllWindows()

# using Pillow for image display
img = Image.open('handwritten test.jpg')
img.show()
