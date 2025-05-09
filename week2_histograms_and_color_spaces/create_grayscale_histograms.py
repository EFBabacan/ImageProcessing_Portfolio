from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Path to your image file.
IMAGE_PATH = "sample_images/foto1.jpeg"

try:
    # Open the image and convert it to grayscale
    img_pil = Image.open(IMAGE_PATH).convert("L")  # "L" mode for grayscale
    img_array = np.array(img_pil)

    # --- Plotting histograms with different bin numbers ---

    # Figure 1: Histogram with 256 bins (each pixel value has its own bin)
    plt.figure(figsize=(10, 4))  # Optional: Adjust figure size
    plt.subplot(1, 3, 1)  # Create a subplot (1 row, 3 columns, 1st plot)
    # The ravel() function flattens the 2D image array into a 1D array.
    # bins=256 means we want 256 bars in our histogram.
    # range=[0, 256] specifies the range of pixel values (0 to 255).
    plt.hist(img_array.ravel(), bins=256, range=[0, 256], color='gray')
    plt.title(f"Histogram with 256 bins\nImage: {IMAGE_PATH}")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")

    # Figure 2: Histogram with 64 bins
    plt.subplot(1, 3, 2)  # 2nd plot in the 1x3 grid
    plt.hist(img_array.ravel(), bins=64, range=[0, 256], color='gray')
    plt.title(f"Histogram with 64 bins")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")

    # Figure 3: Histogram with 8 bins
    plt.subplot(1, 3, 3)  # 3rd plot in the 1x3 grid
    plt.hist(img_array.ravel(), bins=8, range=[0, 256], color='gray')
    plt.title(f"Histogram with 8 bins")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")

    plt.tight_layout()  # Adjusts subplot params for a tight layout.
    plt.show()  # Display all figures

except FileNotFoundError:
    print(f"Error: The file '{IMAGE_PATH}' was not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")