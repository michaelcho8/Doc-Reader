import os

# Base project directory (absolute path to Doc-Reader)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "img")

# If you want your new sub-folders to be called e.g. "raw_uploads"
NEW_IMAGES_DIR = os.path.join(IMAGES_DIR, "new_img")
PREPROCESSED_IMAGES_DIR = os.path.join(IMAGES_DIR, "preprocessed_images")

# OCR Language global constant
OCR_LANGUAGE = "eng"
