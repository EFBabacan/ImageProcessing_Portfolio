import cv2  # OpenCV for image loading and filtering
import numpy as np
import matplotlib.pyplot as plt

# Path to your image file.
# Make sure "foto1.jpeg" is in the same directory as this script,
# or provide the correct path (e.g., "sample_images/foto1.jpeg").
# Filters are often best demonstrated on images with some noise.
IMAGE_PATH = "foto2.jpeg"

try:
    # Load the image
    original_image_bgr = cv2.imread(IMAGE_PATH)

    if original_image_bgr is None:
        raise FileNotFoundError(f"Image not found or could not be opened: {IMAGE_PATH}")

    # Convert to grayscale for easier filter demonstration (can also be applied to color)
    gray_image = cv2.cvtColor(original_image_bgr, cv2.COLOR_BGR2GRAY)

    # --- Apply Mean Filter with different kernel sizes ---
    # cv2.blur(source_image, (kernel_width, kernel_height))

    # Mean filter with a 3x3 kernel
    kernel_size_3x3 = (3, 3)
    filtered_image_3x3 = cv2.blur(gray_image, kernel_size_3x3)

    # Mean filter with a 7x7 kernel
    kernel_size_7x7 = (7, 7)
    filtered_image_7x7 = cv2.blur(gray_image, kernel_size_7x7)

    # Mean filter with a 11x11 kernel
    kernel_size_11x11 = (11, 11)
    filtered_image_11x11 = cv2.blur(gray_image, kernel_size_11x11)

    print(f"Applied mean filters to '{IMAGE_PATH}'. Displaying results...")

    # --- Display results using Matplotlib ---
    plt.figure(figsize=(15, 5))  # Create a figure window

    # 1. Original Grayscale Image
    plt.subplot(1, 4, 1)  # (rows, columns, plot_number)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Original Grayscale Image')
    plt.axis('off')

    # 2. Filtered Image (3x3 Kernel)
    plt.subplot(1, 4, 2)
    plt.imshow(filtered_image_3x3, cmap='gray')
    plt.title(f'Mean Filter ({kernel_size_3x3[0]}x{kernel_size_3x3[1]})')
    plt.axis('off')

    # 3. Filtered Image (7x7 Kernel)
    plt.subplot(1, 4, 3)
    plt.imshow(filtered_image_7x7, cmap='gray')
    plt.title(f'Mean Filter ({kernel_size_7x7[0]}x{kernel_size_7x7[1]})')
    plt.axis('off')

    # 4. Filtered Image (11x11 Kernel)
    plt.subplot(1, 4, 4)
    plt.imshow(filtered_image_11x11, cmap='gray')
    plt.title(f'Mean Filter ({kernel_size_11x11[0]}x{kernel_size_11x11[1]})')
    plt.axis('off')

    plt.tight_layout()  # Adjust layout
    plt.show()  # Display the figure

except FileNotFoundError as fnf_error:
    print(fnf_error)
except Exception as e:
    import traceback

    print(f"An unexpected error occurred: {e}")
    traceback.print_exc()