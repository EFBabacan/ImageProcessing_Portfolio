from PIL import Image
import matplotlib.pyplot as plt # For displaying the image
# import numpy as np # Not strictly necessary here as plt.imshow can handle PIL Image objects

# Path to the image to be used.
# Make sure this path points to an actual image file on your system.
# You should change "foto1.jpeg" to your actual image file name if it's different.
IMAGE_PATH = "sample_images/foto1.jpeg"

try:
    # Open the image using Pillow (PIL)
    image_pil = Image.open(IMAGE_PATH)

    # Get resolution (DPI) from image info.
    # The 'jfif_density' key might not always be present in image metadata.
    # It often stores a tuple like (DPI_X, DPI_Y), e.g., (72, 72).
    dpi_info = image_pil.info.get('jfif_density', 'Not specified')

    dpi_display_text = "DPI: Not specified" # Text to show on image title and console
    if dpi_info != 'Not specified':
        if isinstance(dpi_info, (tuple, list)) and len(dpi_info) == 2:
            dpi_display_text = f"DPI: {dpi_info[0]}x{dpi_info[1]}"
        else:
            dpi_display_text = f"DPI Info: {str(dpi_info)}" # If format is unexpected, show raw info
        print(f"Image: '{IMAGE_PATH}' - {dpi_display_text}")
    else:
        print(f"DPI information not found for image '{IMAGE_PATH}'.")


    # --- Section for Displaying the Image ---
    # Create a new figure for plotting; you can set the figure size (optional)
    plt.figure(figsize=(7, 7))

    # Display the PIL image object directly using Matplotlib
    plt.imshow(image_pil)

    # Add a title to the image plot, including the image path and resolution
    title_text = f"Displayed Image: {IMAGE_PATH}\n{dpi_display_text}"
    plt.title(title_text)
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