from PIL import Image
import os
import cv2
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from config import PREPROCESSED_IMAGES_DIR, NEW_IMAGES_DIR

"""
    Preprocesses images from a specified directory by converting them to PNG format, 
    applying grayscale conversion, and thresholding for binary image processing.
    The function performs the following steps:
    1. Iterates through all files in the `NEW_IMAGES_DIR`.
    2. Skips files that are not images or already exist in the `PREPROCESSED_IMAGES_DIR`.
    3. Converts images to PNG format and saves them in the `PREPROCESSED_IMAGES_DIR`.
    4. Applies preprocessing using OpenCV:
       - Converts the image to grayscale.
       - Applies binary thresholding using Otsu's method.
       - Saves the processed image back to the `PREPROCESSED_IMAGES_DIR`.
    Directories:
    - `NEW_IMAGES_DIR`: Directory containing the original images.
    - `PREPROCESSED_IMAGES_DIR`: Directory where preprocessed images are saved.
    Requirements:
    - The directories `NEW_IMAGES_DIR` and `PREPROCESSED_IMAGES_DIR` must be defined globally.
    - The function uses the `os`, `Pillow`, and `cv2` libraries for file handling and image processing.
    Note:
    - Non-image files are skipped during processing.
    - Existing preprocessed images are not overwritten.
    Raises:
    - FileNotFoundError: If the input file does not exist.
    - ValueError: If the image cannot be processed due to invalid format or other issues.
    """

def preprocess_images():
    
    # Creates main file path and list of files to preprocess
    file_path = os.path.join(NEW_IMAGES_DIR, "handwritten test.jpg")
    png_filename = os.path.splitext(filename)[0] + ".png"

    # Create directory for preprocessed images
    os.makedirs(PREPROCESSED_IMAGES_DIR, exist_ok=True)

    # For each file in new_images_dir
    for filename in os.listdir(NEW_IMAGES_DIR):
        file_path = os.path.join(NEW_IMAGES_DIR, filename)
        png_filename = os.path.splitext(filename)[0] + ".png"
        png_path = os.path.join(PREPROCESSED_IMAGES_DIR, png_filename)
        
        # Skip non-image files
        if os.path.exists(png_path):
            return

        # Convert to PNG
        img = Image.open(file_path).convert("RGB")
        img_np = np.array(img)
        gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)

        png_filename = os.path.splitext(filename)[0] + ".png"
        png_path = os.path.join(PREPROCESSED_IMAGES_DIR, png_filename)
        img.save(png_path, "PNG")

         # Preprocess with OpenCV
        cv_img = cv2.imread(png_path)
        gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY), thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        cv2.imwrite(png_path, thresh)


def convert_to_png(image_path):
    if not image_path.lower().endswith(".png"):
        img = Image.open(image_path).convert("RGB")
        new_path = os.path.splitext(image_path)[0] + ".png"
        img.save(new_path, "PNG")
        return new_path
    return image_path