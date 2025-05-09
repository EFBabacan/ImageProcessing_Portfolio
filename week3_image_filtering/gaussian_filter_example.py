import cv2  # OpenCV for image loading and filtering
import numpy as np
import matplotlib.pyplot as plt

# Path to your image file.
# Choose one of your images, e.g., "foto1.jpeg", "foto2.jpg", "flowers.jpg"
IMAGE_PATH = "foto1.jpeg"

try:
    # Load the image in color
    original_image_bgr = cv2.imread(IMAGE_PATH)

    if original_image_bgr is None:
        raise FileNotFoundError(f"Image not found or could not be opened: {IMAGE_PATH}")

    # Convert original BGR to RGB for correct Matplotlib display
    original_image_rgb = cv2.cvtColor(original_image_bgr, cv2.COLOR_BGR2RGB)

    # Convert to grayscale for grayscale filtering example
    gray_image = cv2.cvtColor(original_image_bgr, cv2.COLOR_BGR2GRAY)

    # --- Apply Gaussian Filter ---
    # cv2.GaussianBlur(source_image, (kernel_width, kernel_height), sigmaX, [sigmaY])
    # kernel_width and kernel_height must be positive and odd.
    # sigmaX is Gaussian kernel standard deviation in X direction.
    # If sigmaY is zero, it is set to be equal to sigmaX.
    # If both sigmas are zeros, they are computed from kernel_size.

    # Example 1: Grayscale image, 5x5 kernel, sigma calculated by OpenCV
    kernel_size1 = (5, 5)
    sigma1 = 0
    filtered_gray_1 = cv2.GaussianBlur(gray_image, kernel_size1, sigma1)

    # Example 2: Grayscale image, 11x11 kernel, sigma calculated by OpenCV
    kernel_size2 = (11, 11)
    sigma2 = 0
    filtered_gray_2 = cv2.GaussianBlur(gray_image, kernel_size2, sigma2)

    # Example 3: Color image, 7x7 kernel, specific sigma values
    kernel_size3 = (7, 7)
    sigma3_x = 1.5
    sigma3_y = 1.5  # Can be different, or 0 to be same as sigma3_x
    filtered_color_bgr = cv2.GaussianBlur(original_image_bgr, kernel_size3, sigma3_x, sigmaY=sigma3_y)
    # Convert BGR to RGB for displaying the filtered color image
    filtered_color_rgb = cv2.cvtColor(filtered_color_bgr, cv2.COLOR_BGR2RGB)

    print(f"Applied Gaussian filters to '{IMAGE_PATH}'. Displaying results...")

    # --- Display results using Matplotlib ---
    plt.figure(figsize=(16, 10))

    # 1. Original Color Image
    plt.subplot(2, 3, 1)
    plt.imshow(original_image_rgb)
    plt.title('Original Color Image')
    plt.axis('off')

    # 2. Original Grayscale Image
    plt.subplot(2, 3, 2)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Original Grayscale')
    plt.axis('off')

    # (Empty subplot for spacing or another image later)
    # plt.subplot(2, 3, 3)
    # plt.axis('off')

    # 4. Filtered Grayscale Image (Kernel 5x5, Sigma auto)
    plt.subplot(2, 3, 4)
    plt.imshow(filtered_gray_1, cmap='gray')
    plt.title(f'Gaussian Filter (Gray)\nKernel: {kernel_size1}, Sigma: Auto')
    plt.axis('off')

    # 5. Filtered Grayscale Image (Kernel 11x11, Sigma auto)
    plt.subplot(2, 3, 5)
    plt.imshow(filtered_gray_2, cmap='gray')
    plt.title(f'Gaussian Filter (Gray)\nKernel: {kernel_size2}, Sigma: Auto')
    plt.axis('off')

    # 6. Filtered Color Image (Kernel 7x7, Sigma 1.5)
    plt.subplot(2, 3, 6)
    plt.imshow(filtered_color_rgb)
    plt.title(f'Gaussian Filter (Color)\nKernel: {kernel_size3}, Sigma: {sigma3_x}')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

except FileNotFoundError as fnf_error:
    print(fnf_error)
except Exception as e:
    import traceback

    print(f"An unexpected error occurred: {e}")
    traceback.print_exc()