import cv2  # OpenCV for image processing and histogram calculation
import numpy as np
import matplotlib.pyplot as plt

# Path to your image file.


IMAGE_PATH = "sample_images/foto1.jpeg"

try:
    # Load the color image using OpenCV
    # cv2.imread() loads images in BGR (Blue, Green, Red) order by default.
    color_image_bgr = cv2.imread(IMAGE_PATH)

    if color_image_bgr is None:
        raise FileNotFoundError(f"Image not found or could not be opened: {IMAGE_PATH}")

    # Load the image in grayscale using OpenCV
    # The '0' flag loads the image as grayscale.
    gray_image = cv2.imread(IMAGE_PATH, 0)

    if gray_image is None:  # Should not happen if color_image_bgr loaded, but good practice
        raise FileNotFoundError(f"Grayscale image not found or could not be opened: {IMAGE_PATH}")

    # Define colors for plotting each histogram line
    # OpenCV loads as BGR, so channel 0 is Blue, 1 is Green, 2 is Red.
    plot_colors = ('blue', 'green', 'red', 'gray')
    channel_labels = ('Blue Channel', 'Green Channel', 'Red Channel', 'Grayscale')

    plt.figure(figsize=(10, 6))
    plt.title(f'Color and Grayscale Histograms for {IMAGE_PATH}')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Number of Pixels')

    # Calculate and plot histogram for each color channel (B, G, R)
    for i, color_name in enumerate(plot_colors):
        if i < 3:  # For B, G, R channels
            # cv2.calcHist([images], [channels], mask, [histSize], ranges)
            # For BGR image: channel 0 is Blue, 1 is Green, 2 is Red
            histogram = cv2.calcHist([color_image_bgr], [i], None, [256], [0, 256])
            plt.plot(histogram, color=color_name, label=channel_labels[i])
            print(f"Calculated histogram for {channel_labels[i]}")
        elif i == 3:  # For Grayscale
            histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
            plt.plot(histogram, color=color_name, label=channel_labels[i])
            print(f"Calculated histogram for {channel_labels[i]}")

    plt.xlim([0, 256])  # Set x-axis limits for pixel intensity
    plt.legend()  # Show legend to identify lines
    plt.grid(True, linestyle='--', alpha=0.7)  # Add a grid for better readability
    plt.tight_layout()
    plt.show()

except FileNotFoundError as fnf_error:
    print(fnf_error)
except Exception as e:
    import traceback

    print(f"An unexpected error occurred: {e}")
    traceback.print_exc()