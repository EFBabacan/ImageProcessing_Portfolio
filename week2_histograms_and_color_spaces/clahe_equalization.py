import cv2  # OpenCV for image loading and CLAHE
import numpy as np
import matplotlib.pyplot as plt

# Path to your image file.
# Ensure "foto1.jpeg" is in the same directory as this script,
# or provide the correct path (e.g., "sample_images/foto1.jpeg").
IMAGE_PATH = "foto1.jpeg"

try:
    # Load the image in grayscale using OpenCV
    gray_image = cv2.imread(IMAGE_PATH, 0)

    if gray_image is None:
        raise FileNotFoundError(f"Image not found or could not be opened: {IMAGE_PATH}")

    # --- Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) ---
    # Create a CLAHE object. Parameters can be adjusted:
    # clipLimit: Threshold for contrast limiting. Higher means more contrast.
    # tileGridSize: Size of the grid for localized equalization (e.g., (8,8)).
    clahe_object = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

    # Apply CLAHE to the grayscale image
    clahe_image = clahe_object.apply(gray_image)

    # --- Calculate Histograms for both images ---
    # Calculate histogram for the original grayscale image
    original_hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    # Calculate histogram for the CLAHE processed image
    clahe_hist = cv2.calcHist([clahe_image], [0], None, [256], [0, 256])

    # --- Display results using Matplotlib in a 2x2 grid ---
    plt.figure(figsize=(12, 10))  # Create a figure window

    # 1. Original Image
    plt.subplot(2, 2, 1)  # (rows, columns, plot_number)
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

    # 3. CLAHE Equalized Image
    plt.subplot(2, 2, 3)
    plt.imshow(clahe_image, cmap='gray')
    plt.title('CLAHE Equalized Image')
    plt.axis('off')

    # 4. CLAHE Equalized Histogram
    plt.subplot(2, 2, 4)
    plt.plot(clahe_hist, color='blue')
    plt.title('CLAHE Equalized Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Number of Pixels')
    plt.xlim([0, 256])
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout()  # Adjust layout
    plt.show()  # Display the figure

except FileNotFoundError as fnf_error:
    print(fnf_error)
except Exception as e:
    import traceback

    print(f"An unexpected error occurred: {e}")
    traceback.print_exc()