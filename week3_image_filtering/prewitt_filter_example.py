import cv2  # OpenCV for image loading and custom filtering
import numpy as np
import matplotlib.pyplot as plt

# Path to your image file.
IMAGE_PATH = "sample_images/foto1.jpeg"  # Or choose another image

try:
    # Load the image
    original_image_bgr = cv2.imread(IMAGE_PATH)

    if original_image_bgr is None:
        raise FileNotFoundError(f"Image not found or could not be opened: {IMAGE_PATH}")

    # Convert to grayscale
    gray_image = cv2.cvtColor(original_image_bgr, cv2.COLOR_BGR2GRAY)

    # --- Define Prewitt Kernels ---
    # Gx kernel for detecting vertical edges
    kernel_prewitt_x = np.array([[-1, 0, 1],
                                 [-1, 0, 1],
                                 [-1, 0, 1]], dtype=np.float32)

    # Gy kernel for detecting horizontal edges
    kernel_prewitt_y = np.array([[1, 1, 1],
                                 [0, 0, 0],
                                 [-1, -1, -1]], dtype=np.float32)

    # --- Apply Prewitt Filter using cv2.filter2D() ---
    # cv2.filter2D(src, ddepth, kernel)
    # ddepth: Output image depth. Using -1 means output has same depth as source.
    #         For gradient operators, it's better to use a signed type like cv2.CV_64F
    #         to capture both positive and negative slopes, then take absolute.

    # Apply Gx kernel
    prewitt_x = cv2.filter2D(gray_image, cv2.CV_64F, kernel_prewitt_x)
    prewitt_x_abs = np.absolute(prewitt_x)
    prewitt_x_uint8 = np.uint8(prewitt_x_abs)

    # Apply Gy kernel
    prewitt_y = cv2.filter2D(gray_image, cv2.CV_64F, kernel_prewitt_y)
    prewitt_y_abs = np.absolute(prewitt_y)
    prewitt_y_uint8 = np.uint8(prewitt_y_abs)

    # Combine Gx and Gy to get the magnitude of the gradient
    # Magnitude = sqrt(Gx^2 + Gy^2)
    gradient_magnitude = np.sqrt(prewitt_x ** 2 + prewitt_y ** 2)
    # Normalize and convert for display
    gradient_magnitude_normalized = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)
    gradient_magnitude_uint8 = np.uint8(gradient_magnitude_normalized)

    print(f"Applied Prewitt filters to '{IMAGE_PATH}'. Displaying results...")

    # --- Display results using Matplotlib ---
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Original Grayscale Image')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(prewitt_x_uint8, cmap='gray')
    plt.title('Prewitt X (Vertical Edges)')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(prewitt_y_uint8, cmap='gray')
    plt.title('Prewitt Y (Horizontal Edges)')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.imshow(gradient_magnitude_uint8, cmap='gray')
    plt.title('Prewitt Gradient Magnitude')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

except FileNotFoundError as fnf_error:
    print(fnf_error)
except Exception as e:
    import traceback

    print(f"An unexpected error occurred: {e}")
    traceback.print_exc()