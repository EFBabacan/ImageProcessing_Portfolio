import cv2  # For image loading
import numpy as np
import matplotlib.pyplot as plt
import random  # For adding salt-and-pepper noise (from previous example)

# Path to your image file.
IMAGE_PATH = "sample_images/flowers.png"  # Or choose another image


def add_salt_and_pepper_noise(image_array, amount=0.05):
    """Adds salt and pepper noise to a grayscale image (NumPy array)."""
    output_image = np.copy(image_array)
    num_salt = np.ceil(amount * image_array.size * 0.5)
    coords_salt = [np.random.randint(0, i - 1, int(num_salt)) for i in image_array.shape[:2]]
    if output_image.ndim == 2:  # Grayscale
        output_image[coords_salt[0], coords_salt[1]] = 255
    else:  # Color (apply to all channels or just one for visual effect)
        output_image[coords_salt[0], coords_salt[1], :] = 255

    num_pepper = np.ceil(amount * image_array.size * 0.5)
    coords_pepper = [np.random.randint(0, i - 1, int(num_pepper)) for i in image_array.shape[:2]]
    if output_image.ndim == 2:  # Grayscale
        output_image[coords_pepper[0], coords_pepper[1]] = 0
    else:  # Color
        output_image[coords_pepper[0], coords_pepper[1], :] = 0

    return output_image


def conservative_smoother(image_array, kernel_size):
    """
    Applies Conservative Smoothing to a grayscale image (NumPy array).
    Args:
        image_array (np.array): Input grayscale image.
        kernel_size (int): Size of the square kernel (must be odd, e.g., 3, 5).
    Returns:
        np.array: Smoothed grayscale image.
    """
    if kernel_size % 2 == 0:
        raise ValueError("Kernel size must be an odd integer.")

    k_half = kernel_size // 2
    rows, cols = image_array.shape
    output_image = np.copy(image_array)  # Start with a copy of the original

    # Pad the image to handle borders
    # This simplifies kernel operations near the image edges.
    padded_image = np.pad(image_array, pad_width=k_half, mode='edge')

    for r in range(rows):
        for c in range(cols):
            # Current pixel in the original image corresponds to (r+k_half, c+k_half) in padded image
            center_pixel_value = image_array[r, c]

            # Extract the kernel window from the padded image
            # The window is centered around the current pixel's equivalent in the padded image
            kernel_window = padded_image[r: r + kernel_size, c: c + kernel_size]

            min_val_in_window = np.min(kernel_window)
            max_val_in_window = np.max(kernel_window)

            if center_pixel_value < min_val_in_window:
                output_image[r, c] = min_val_in_window
            elif center_pixel_value > max_val_in_window:
                output_image[r, c] = max_val_in_window
            # else: the pixel value remains unchanged (already handled by np.copy)

    return output_image


try:
    # Load the image
    original_image_bgr = cv2.imread(IMAGE_PATH)
    if original_image_bgr is None:
        raise FileNotFoundError(f"Image not found or could not be opened: {IMAGE_PATH}")

    # Convert to grayscale
    gray_image = cv2.cvtColor(original_image_bgr, cv2.COLOR_BGR2GRAY)

    # Add salt and pepper noise
    noisy_image = add_salt_and_pepper_noise(gray_image, amount=0.05)

    # --- Apply Conservative Smoothing ---
    kernel_s = 3  # Kernel size (e.g., 3 for 3x3, 5 for 5x5)
    smoothed_image = conservative_smoother(noisy_image, kernel_s)

    kernel_s_large = 5
    smoothed_image_large_kernel = conservative_smoother(noisy_image, kernel_s_large)

    print(f"Applied Conservative Smoothing to noisy version of '{IMAGE_PATH}'. Displaying results...")

    # --- Display results ---
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
    plt.imshow(smoothed_image, cmap='gray')
    plt.title(f'Conservative Smoothing (Kernel {kernel_s}x{kernel_s})')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.imshow(smoothed_image_large_kernel, cmap='gray')
    plt.title(f'Conservative Smoothing (Kernel {kernel_s_large}x{kernel_s_large})')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

except FileNotFoundError as fnf_error:
    print(fnf_error)
except Exception as e:
    import traceback

    print(f"An unexpected error occurred: {e}")
    traceback.print_exc()