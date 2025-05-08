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

    # --- Convert RGB to HSV using Pillow ---
    # Pillow's convert method makes this very easy!
    hsv_image = rgb_image.convert('HSV')

    # --- Separate HSV channels for visualization ---
    # Although we have the hsv_image object, visualizing its channels requires
    # splitting them. We can convert to numpy array first for easier splitting.
    hsv_array = np.array(hsv_image)

    # H channel (Hue) - Represents the color type
    h_channel = hsv_array[:, :, 0]
    # S channel (Saturation) - Represents the color purity/intensity
    s_channel = hsv_array[:, :, 1]
    # V channel (Value) - Represents the brightness
    v_channel = hsv_array[:, :, 2]

    print(f"Converted '{IMAGE_PATH}' from RGB to HSV color space.")
    print(f"Image dimensions (H, W, Channels): {hsv_array.shape}")

    # --- Display results using Matplotlib in a 2x2 grid ---
    plt.figure(figsize=(10, 10))

    # 1. Original RGB Image
    plt.subplot(2, 2, 1)
    plt.imshow(rgb_image)  # Display original RGB
    plt.title('Original RGB Image')
    plt.axis('off')

    # 2. Hue Channel (H)
    plt.subplot(2, 2, 2)
    plt.imshow(h_channel, cmap='hsv')  # Use 'hsv' colormap for Hue visualization
    plt.title('Hue Channel (H)')
    plt.axis('off')

    # 3. Saturation Channel (S)
    plt.subplot(2, 2, 3)
    plt.imshow(s_channel, cmap='gray')  # Saturation is often viewed as grayscale intensity
    plt.title('Saturation Channel (S)')
    plt.axis('off')

    # 4. Value Channel (V)
    plt.subplot(2, 2, 4)
    plt.imshow(v_channel, cmap='gray')  # Value (brightness) is also viewed as grayscale
    plt.title('Value Channel (V)')
    plt.axis('off')

    plt.tight_layout()  # Adjust layout
    plt.show()  # Display the figure

except FileNotFoundError as fnf_error:
    print(fnf_error)
except Exception as e:
    import traceback

    print(f"An unexpected error occurred: {e}")
    traceback.print_exc()