import cv2 # OpenCV for image loading and histogram equalization
import numpy as np
import matplotlib.pyplot as plt

# Path to your image file.
# Ensure "foto1.jpeg" is in the same directory as this script,
# or provide the correct path (e.g., "sample_images/foto1.jpeg").
IMAGE_PATH = "foto1.jpeg"

try:
    # Load the image in grayscale using OpenCV
    # The '0' flag ensures it's loaded as grayscale.
    gray_image = cv2.imread(IMAGE_PATH, 0)

    if gray_image is None:
        raise FileNotFoundError(f"Image not found or could not be opened: {IMAGE_PATH}")

    # --- Apply Histogram Equalization ---
    # cv2.equalizeHist() applies histogram equalization on the grayscale image.
    equalized_image = cv2.equalizeHist(gray_image)

    # --- Calculate Histograms for both images ---
    # Calculate histogram for the original grayscale image
    original_hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    # Calculate histogram for the equalized grayscale image
    equalized_hist = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

    # --- Display results using Matplotlib in a 2x2 grid ---
    plt.figure(figsize=(12, 10)) # Create a figure window

    # 1. Original Image
    plt.subplot(2, 2, 1) # (rows, columns, plot_number)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Original Grayscale Image')
    plt.axis('off')

    # 2. Original Histogram
    plt.subplot(2, 2, 2)
    plt.plot(original_hist, color='black')
    plt.title('Original Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Number of Pixels')
    plt.xlim([0, 256])
    plt.grid(True, linestyle='--', alpha=0.7)

    # 3. Equalized Image
    plt.subplot(2, 2, 3)
    plt.imshow(equalized_image, cmap='gray')
    plt.title('Equalized Image')
    plt.axis('off')

    # 4. Equalized Histogram
    plt.subplot(2, 2, 4)
    plt.plot(equalized_hist, color='blue')
    plt.title('Equalized Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Number of Pixels')
    plt.xlim([0, 256])
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout() # Adjust layout to prevent overlapping titles/labels
    plt.show() # Display the figure with all subplots

except FileNotFoundError as fnf_error:
    print(fnf_error)
except Exception as e:
    import traceback
    print(f"An unexpected error occurred: {e}")
    traceback.print_exc()