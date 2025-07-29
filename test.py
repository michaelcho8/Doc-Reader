import cv2
import matplotlib.pyplot as plt
import requests
import numpy as np

# URL of the image to download
image_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/JIMMY_ANDRES_PALOMA.jpg"
try:
    # Download the image from the internet
    response = requests.get(image_url, stream=True)
    response.raise_for_status()
    if response.status_code != 200:
        raise Exception(f"Failed to download image. Status code: {response.status_code}")

    # Convert the downloaded content to a numpy array
    image_array = np.asarray(bytearray(response.raw.read()), dtype=np.uint8)
    gray = cv2.imdecode(image_array, cv2.IMREAD_GRAYSCALE)

    # Check if the image was loaded successfully
    if gray is None:
        raise Exception("Failed to decode the image from the downloaded content.")

    # Apply Otsu's thresholding
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Display the original and thresholded images
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Original Grayscale Image")
    plt.imshow(gray, cmap="gray")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.title("Thresholded Image")
    plt.imshow(thresh, cmap="gray")
    plt.axis("off")

    plt.show()

except requests.exceptions.RequestException as e:
    print(f"Failed to download image: {e}")
except Exception as e:
    print(f"An error occured {e}")