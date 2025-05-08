from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Path to your image file.
# Ensure "foto1.jpeg" is in the same directory as this script,
# or provide the correct path (e.g., "sample_images/foto1.jpeg").
IMAGE_PATH = "foto1.jpeg"

try:
    # Load the RGB image using Pillow
    rgb_image = Image.open(IMAGE_PATH).convert('RGB')  # Ensure it's in RGB mode

    if rgb_image is None:
        raise FileNotFoundError(f"Image not found or could not be opened: {IMAGE_PATH}")

    # --- Convert RGB to CMYK using Pillow ---
    # Pillow's convert method handles CMYK conversion directly.
    cmyk_image = rgb_image.convert('CMYK')

    # --- Separate CMYK channels for visualization ---
    # Use Pillow's split() method to get individual channels
    c_channel, m_channel, y_channel, k_channel = cmyk_image.split()

    print(f"Converted '{IMAGE_PATH}' from RGB to CMYK color space.")

    # --- Display results using Matplotlib ---
    # We will display 5 images: Original RGB and the 4 CMYK channels
    plt.figure(figsize=(12, 8))

    # 1. Original RGB Image
    plt.subplot(2, 3, 1)  # Arrange in 2 rows, 3 columns
    plt.imshow(rgb_image)
    plt.title('Original RGB Image')
    plt.axis('off')

    # 2. Cyan Channel (C)
    plt.subplot(2, 3, 2)
    # Channels usually represent ink density, often visualized inverted or as grayscale
    plt.imshow(np.array(c_channel), cmap='gray')
    plt.title('Cyan Channel (C)')
    plt.axis('off')

    # 3. Magenta Channel (M)
    plt.subplot(2, 3, 3)
    plt.imshow(np.array(m_channel), cmap='gray')
    plt.title('Magenta Channel (M)')
    plt.axis('off')

    # 4. Yellow Channel (Y)
    plt.subplot(2, 3, 4)
    plt.imshow(np.array(y_channel), cmap='gray')
    plt.title('Yellow Channel (Y)')
    plt.axis('off')

    # 5. Key/Black Channel (K)
    plt.subplot(2, 3, 5)
    plt.imshow(np.array(k_channel), cmap='gray')
    plt.title('Key/Black Channel (K)')
    plt.axis('off')

    # Adjust layout and display
    plt.tight_layout()
    plt.show()

except FileNotFoundError as fnf_error:
    print(fnf_error)
except Exception as e:
    import traceback

    print(f"An unexpected error occurred: {e}")
    traceback.print_exc()