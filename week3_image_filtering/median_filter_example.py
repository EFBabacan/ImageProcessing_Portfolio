import cv2  # OpenCV for image loading and filtering
import numpy as np
import matplotlib.pyplot as plt
import random  # For adding salt-and-pepper noise

# Path to your image file.
IMAGE_PATH = "sample_images/flowers.png"



def add_salt_and_pepper_noise(image, amount=0.05):
    """
    Adds salt and pepper noise to a grayscale image.
    Args:
        image (np.array): Grayscale input image.
        amount (float): Proportion of pixels to be replaced by noise (0.0 to 1.0).
    Returns:
        np.array: Image with salt and pepper noise.
    """
    noisy_image = np.copy(image)
    # Salt noise (white pixels)
    num_salt = np.ceil(amount * image.size * 0.5)  # 0.5 for half salt, half pepper
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy_image[coords[0], coords[1]] = 255

    # Pepper noise (black pixels)
    num_pepper = np.ceil(amount * image.size * 0.5)
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy_image[coords[0], coords[1]] = 0

    return noisy_image


try:
    # Load the image
    original_image_bgr = cv2.imread(IMAGE_PATH)

    if original_image_bgr is None:
        raise FileNotFoundError(f"Image not found or could not be opened: {IMAGE_PATH}")

    # Convert to grayscale
    gray_image = cv2.cvtColor(original_image_bgr, cv2.COLOR_BGR2GRAY)

    # Add salt and pepper noise to the grayscale image
    noisy_image = add_salt_and_pepper_noise(gray_image, amount=0.05)  # 5% noise

    # --- Apply Median Filter with different kernel sizes ---
    # cv2.medianBlur(source_image, kernel_size)
    # kernel_size must be an odd integer (e.g., 3, 5, 7).

    # Median filter with a 3x3 kernel (kernel_size = 3)
    filtered_image_k3 = cv2.medianBlur(noisy_image, 1)

    # Median filter with a 5x5 kernel (kernel_size = 5)
    filtered_image_k5 = cv2.medianBlur(noisy_image, 5)

    print(f"Applied median filters to noisy version of '{IMAGE_PATH}'. Displaying results...")

    # --- Display results using Matplotlib ---
    plt.figure(figsize=(15, 10))

    plt.subplot(2, 2, 1)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Original Grayscale Image')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(noisy_image, cmap='gray')
    plt.title('Image with Salt & Pepper Noise')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(filtered_image_k3, cmap='gray')
    plt.title('Median Filter (Kernel Size 1)')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.imshow(filtered_image_k5, cmap='gray')
    plt.title('Median Filter (Kernel Size 5)')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

except FileNotFoundError as fnf_error:
    print(fnf_error)
except Exception as e:
    import traceback

    print(f"An unexpected error occurred: {e}")
    traceback.print_exc()