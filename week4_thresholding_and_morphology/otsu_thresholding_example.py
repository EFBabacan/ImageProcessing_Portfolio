import cv2  # OpenCV for image loading and Otsu's thresholding
import numpy as np
import matplotlib.pyplot as plt

# Path to your image file within the sample_images subfolder of week4.
IMAGE_PATH = "sample_images/foto1.jpeg"  # Or choose an image that might be bimodal

try:
    # Load the image in grayscale
    gray_image = cv2.imread(IMAGE_PATH, 0)

    if gray_image is None:
        raise FileNotFoundError(f"Image not found or could not be opened: {IMAGE_PATH}")

    # --- Apply Otsu's Thresholding using OpenCV ---
    # When cv2.THRESH_OTSU is used, the threshold value (second argument to cv2.threshold)
    # is calculated automatically. So, we can pass 0 as a placeholder.
    # The function returns the optimal threshold value (ret_otsu) and the thresholded image.
    # We combine THRESH_BINARY with THRESH_OTSU.

    # Global thresholding with Otsu's method
    ret_otsu, thresh_otsu = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    print(f"Applied Otsu's thresholding to '{IMAGE_PATH}'.")
    print(f"Optimal threshold value found by Otsu's method: {ret_otsu}")

    # --- Display results using Matplotlib ---
    plt.figure(figsize=(15, 5))

    # 1. Original Grayscale Image
    plt.subplot(1, 3, 1)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Original Grayscale Image')
    plt.axis('off')

    # 2. Histogram of the Grayscale Image (to see if it's bimodal)
    plt.subplot(1, 3, 2)
    plt.hist(gray_image.ravel(), bins=256, range=[0, 256], color='gray', alpha=0.75)
    # Plot a vertical line at the threshold found by Otsu
    plt.axvline(ret_otsu, color='red', linestyle='dashed', linewidth=2, label=f'Otsu Threshold: {ret_otsu:.0f}')
    plt.title('Grayscale Histogram & Otsu\'s Threshold')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Number of Pixels')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)

    # 3. Otsu's Thresholded Image
    plt.subplot(1, 3, 3)
    plt.imshow(thresh_otsu, cmap='gray')
    plt.title(f'Otsu\'s Binarization (Thresh={ret_otsu:.0f})')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

except FileNotFoundError as fnf_error:
    print(fnf_error)
except Exception as e:
    import traceback

    print(f"An unexpected error occurred: {e}")
    traceback.print_exc()