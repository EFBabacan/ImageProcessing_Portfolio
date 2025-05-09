from PIL import Image
import numpy as np
import matplotlib.pyplot as plt  # Import the Matplotlib library for plotting

# Path to the image to be used.
# If in a subfolder like 'sample_images', it should be 'sample_images/img1.jpg'.
# Make sure this path points to an actual image file on your system.

IMAGE_PATH = "sample_images/foto1.jpeg"

try:
    # Open the image using Pillow (PIL)
    img_pil = Image.open(IMAGE_PATH)
    # Convert the PIL image to grayscale ("L" mode)
    img_gray_pil = img_pil.convert("L")
    # Convert the grayscale PIL image to a NumPy array
    img_array = np.array(img_gray_pil)

    # Print the dimensions (height, width) of the image array to the console
    print(f"The dimensions (height, width) of image '{IMAGE_PATH}': {img_array.shape}")

    # --- Section for Displaying the Image ---
    # Create a new figure for plotting; you can set the figure size (optional)
    plt.figure(figsize=(6, 6))

    # Display the NumPy array as an image.
    # Using cmap='gray' is important for showing grayscale images correctly.
    plt.imshow(img_array, cmap='gray')

    # Add a title to the image plot
    plt.title(f"Displayed Image: {IMAGE_PATH}\nDimensions: {img_array.shape}")
    # Turn off the axis numbers and ticks for a cleaner look (optional)
    plt.axis('off')
    # Show the plot on the screen
    plt.show()

except FileNotFoundError:
    # Handle the case where the image file is not found
    print(f"Error: The file '{IMAGE_PATH}' was not found. Please check the file path.")
except Exception as e:
    # Handle any other potential errors during the process
    print(f"An error occurred: {e}")