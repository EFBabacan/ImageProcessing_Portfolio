import cv2  # OpenCV for image loading and thresholding
import numpy as np
import matplotlib.pyplot as plt

# Path to your image file within the sample_images subfolder of week4.
# Make sure to create 'week4_thresholding_and_morphology/sample_images/'
# and place your image there.
IMAGE_PATH = "sample_images/foto1.jpeg"  # Or choose another image like 'flowers.jpg'

try:
    # Load the image in grayscale
    gray_image = cv2.imread(IMAGE_PATH, 0)

    if gray_image is None:
        raise FileNotFoundError(f"Image not found or could not be opened: {IMAGE_PATH}")

    # --- Apply Static Thresholding using OpenCV ---
    # cv2.threshold(source_image, threshold_value, max_value, threshold_type)
    # threshold_value: The threshold value to classify pixel values.
    # max_value: The value to be assigned if pixel value is more than (or less than,
    #            depending on the type) the threshold value. Usually 255 for binary images.

    # We'll use a common threshold value, e.g., 127.
    # You can experiment with different values (0-255).
    thresh_val = 127
    max_val = 255

    # 1. Binary Thresholding (cv2.THRESH_BINARY)
    # If pixel_value > thresh_val, new_value = max_val, else new_value = 0
    ret1, thresh_binary = cv2.threshold(gray_image, thresh_val, max_val, cv2.THRESH_BINARY)

    # 2. Inverse Binary Thresholding (cv2.THRESH_BINARY_INV)
    # If pixel_value > thresh_val, new_value = 0, else new_value = max_val
    ret2, thresh_binary_inv = cv2.threshold(gray_image, thresh_val, max_val, cv2.THRESH_BINARY_INV)

    # 3. Truncate Thresholding (cv2.THRESH_TRUNC)
    # If pixel_value > thresh_val, new_value = thresh_val, else new_value = pixel_value (unchanged)
    ret3, thresh_trunc = cv2.threshold(gray_image, thresh_val, max_val, cv2.THRESH_TRUNC)

    # 4. Threshold to Zero (cv2.THRESH_TOZERO)
    # If pixel_value > thresh_val, new_value = pixel_value (unchanged), else new_value = 0
    ret4, thresh_tozero = cv2.threshold(gray_image, thresh_val, max_val, cv2.THRESH_TOZERO)

    # 5. Inverse Threshold to Zero (cv2.THRESH_TOZERO_INV)
    # If pixel_value > thresh_val, new_value = 0, else new_value = pixel_value (unchanged)
    ret5, thresh_tozero_inv = cv2.threshold(gray_image, thresh_val, max_val, cv2.THRESH_TOZERO_INV)

    print(f"Applied static thresholding types to '{IMAGE_PATH}' with threshold={thresh_val}. Displaying results...")

    # --- Display results using Matplotlib ---
    titles = [
        'Original Grayscale Image', f'Binary (thresh={thresh_val})', f'Binary Inverse (thresh={thresh_val})',
        f'Truncate (thresh={thresh_val})', f'To Zero (thresh={thresh_val})', f'To Zero Inverse (thresh={thresh_val})'
    ]
    images = [
        gray_image, thresh_binary, thresh_binary_inv,
        thresh_trunc, thresh_tozero, thresh_tozero_inv
    ]

    plt.figure(figsize=(15, 10))  # Adjust figure size for 6 images

    for i in range(6):
        plt.subplot(2, 3, i + 1)  # 2 rows, 3 columns
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')

    plt.tight_layout()
    plt.show()

except FileNotFoundError as fnf_error:
    print(fnf_error)
except Exception as e:
    import traceback

    print(f"An unexpected error occurred: {e}")
    traceback.print_exc()