import cv2  # OpenCV for image loading and Laplacian filter
import numpy as np
import matplotlib.pyplot as plt

# Path to your image file.
# Ensure this path points to an actual image file in your sample_images subfolder.
IMAGE_PATH = "sample_images/foto1.jpeg"  # Or use another image like "flowers.jpg"

try:
    # Load the image
    original_image_bgr = cv2.imread(IMAGE_PATH)

    if original_image_bgr is None:
        raise FileNotFoundError(f"Image not found or could not be opened: {IMAGE_PATH}")

    # Convert to grayscale - Laplacian is typically applied to grayscale images
    gray_image = cv2.cvtColor(original_image_bgr, cv2.COLOR_BGR2GRAY)

    # --- Apply Laplacian Filter using OpenCV ---
    # cv2.Laplacian(src, ddepth, ksize)
    # src: Input image
    # ddepth: Output image depth. cv2.CV_64F is often used to capture negative values from derivative,
    #         then take absolute value and convert to uint8.
    # ksize: Size of the Laplacian kernel (must be odd and positive).
    #        Default is 1, which corresponds to the kernel:
    #        [[0, 1, 0],
    #         [1,-4, 1],
    #         [0, 1, 0]] (This is the one PDF Kod 3.6 uses manually)

    # Laplacian with kernel size 1 (uses the 3x3 kernel mentioned above)
    laplacian_k1 = cv2.Laplacian(gray_image, cv2.CV_64F, ksize=1)
    laplacian_k1_abs = np.absolute(laplacian_k1)
    laplacian_k1_uint8 = np.uint8(laplacian_k1_abs)

    # Laplacian with a larger kernel size, e.g., 3 (OpenCV constructs a 3x3 kernel,
    # which is different from ksize=1's specific kernel if not a simple smoothing one before)
    # For ksize=3, OpenCV uses a smoothed second derivative.
    laplacian_k3 = cv2.Laplacian(gray_image, cv2.CV_64F, ksize=3)
    laplacian_k3_abs = np.absolute(laplacian_k3)
    laplacian_k3_uint8 = np.uint8(laplacian_k3_abs)

    # Optional: Apply Gaussian blur before Laplacian to reduce noise sensitivity
    # blurred_image = cv2.GaussianBlur(gray_image, (3,3), 0)
    # laplacian_blurred = cv2.Laplacian(blurred_image, cv2.CV_64F, ksize=1)
    # laplacian_blurred_abs = np.absolute(laplacian_blurred)
    # laplacian_blurred_uint8 = np.uint8(laplacian_blurred_abs)

    print(f"Applied Laplacian filters to '{IMAGE_PATH}'. Displaying results...")

    # --- Display results using Matplotlib ---
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Original Grayscale Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(laplacian_k1_uint8, cmap='gray')
    plt.title('Laplacian Filter (ksize=1)')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(laplacian_k3_uint8, cmap='gray')
    plt.title('Laplacian Filter (ksize=3)')
    plt.axis('off')

    # If you enable the blurred version:
    # plt.subplot(1, 4, 4) # Change subplot grid to (1,4,...)
    # plt.imshow(laplacian_blurred_uint8, cmap='gray')
    # plt.title('Laplacian on Blurred (ksize=1)')
    # plt.axis('off')

    plt.tight_layout()
    plt.show()

except FileNotFoundError as fnf_error:
    print(fnf_error)
except Exception as e:
    import traceback

    print(f"An unexpected error occurred: {e}")
    traceback.print_exc()