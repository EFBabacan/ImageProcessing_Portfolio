import cv2  # OpenCV for image loading and Sobel filter
import numpy as np
import matplotlib.pyplot as plt

# Path to your image file.
# Ensure this path points to an actual image file in your sample_images subfolder.
IMAGE_PATH = "sample_images/glider.jpeg"  # Or choose another image like 'flowers.jpg' for more edges

try:
    # Load the image
    original_image_bgr = cv2.imread(IMAGE_PATH)

    if original_image_bgr is None:
        raise FileNotFoundError(f"Image not found or could not be opened: {IMAGE_PATH}")

    # Convert to grayscale - Sobel is typically applied to grayscale images
    gray_image = cv2.cvtColor(original_image_bgr, cv2.COLOR_BGR2GRAY)

    # --- Apply Sobel Filter using OpenCV ---
    # cv2.Sobel(src, ddepth, dx, dy, ksize)
    # src: Input image
    # ddepth: Output image depth. -1 means the same as input. Using cv2.CV_64F allows for negative gradient values,
    #         then we take absolute value and convert back to uint8.
    # dx: Order of the derivative x. 1 for x-gradient, 0 otherwise.
    # dy: Order of the derivative y. 1 for y-gradient, 0 otherwise.
    # ksize: Size of the Sobel kernel (must be odd, e.g., 1, 3, 5, 7). Default is 3.

    # Calculate Gx (gradient in x-direction - highlights vertical edges)
    sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_x_abs = np.absolute(sobel_x)  # Take absolute value
    sobel_x_uint8 = np.uint8(sobel_x_abs)  # Convert to uint8 for display

    # Calculate Gy (gradient in y-direction - highlights horizontal edges)
    sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
    sobel_y_abs = np.absolute(sobel_y)  # Take absolute value
    sobel_y_uint8 = np.uint8(sobel_y_abs)  # Convert to uint8 for display

    # Combine Gx and Gy to get the magnitude of the gradient
    # Magnitude = sqrt(Gx^2 + Gy^2)
    # cv2.magnitude() can also be used: gradient_magnitude = cv2.magnitude(sobel_x, sobel_y)
    gradient_magnitude = np.sqrt(sobel_x ** 2 + sobel_y ** 2)
    # Normalize and convert for display
    gradient_magnitude_normalized = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)
    gradient_magnitude_uint8 = np.uint8(gradient_magnitude_normalized)

    # Alternative: A simpler way to combine without squaring, good for visualization
    # combined_sobel = cv2.addWeighted(sobel_x_uint8, 0.5, sobel_y_uint8, 0.5, 0)

    print(f"Applied Sobel filters to '{IMAGE_PATH}'. Displaying results...")

    # --- Display results using Matplotlib ---
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Original Grayscale Image')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(sobel_x_uint8, cmap='gray')
    plt.title('Sobel X (Vertical Edges)')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(sobel_y_uint8, cmap='gray')
    plt.title('Sobel Y (Horizontal Edges)')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.imshow(gradient_magnitude_uint8, cmap='gray')
    plt.title('Sobel Gradient Magnitude')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

except FileNotFoundError as fnf_error:
    print(fnf_error)
except Exception as e:
    import traceback

    print(f"An unexpected error occurred: {e}")
    traceback.print_exc()