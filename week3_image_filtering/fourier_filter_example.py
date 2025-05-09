import cv2  # For image loading
import numpy as np
import matplotlib.pyplot as plt

# Path to your image file.
IMAGE_PATH = "sample_images/foto1.jpeg"  # Or use an image like "flowers.jpg"

try:
    # Load the image in grayscale
    gray_image = cv2.imread(IMAGE_PATH, 0)

    if gray_image is None:
        raise FileNotFoundError(f"Image not found or could not be opened: {IMAGE_PATH}")

    # --- Step 1: Apply Fourier Transform ---
    # Compute the 2D Discrete Fourier Transform (DFT)
    f_transform = np.fft.fft2(gray_image)

    # Shift the zero-frequency component (DC component) from top-left to the center
    # This makes it easier to visualize and create filters.
    f_transform_shifted = np.fft.fftshift(f_transform)

    # Calculate the magnitude spectrum (for visualization)
    # Use log scale for better visibility of frequency components
    magnitude_spectrum = 20 * np.log(np.abs(f_transform_shifted) + 1)  # Add 1 to avoid log(0)

    # --- Step 2: Create a Frequency Domain Filter (Low-Pass Filter Example) ---
    rows, cols = gray_image.shape
    center_row, center_col = rows // 2, cols // 2

    # Create a circular Low-Pass Filter (LPF) mask
    # This mask will allow low frequencies (near the center) to pass and block high frequencies.
    radius = 30  # Cut-off frequency: determines how much blurring. Smaller radius = more blur.
    mask = np.zeros((rows, cols), np.uint8)
    # Create a circle in the mask
    cv2.circle(mask, (center_col, center_row), radius, 1, thickness=-1)  # 1 for pass, 0 for block

    # --- Step 3: Apply the filter in Frequency Domain ---
    f_transform_shifted_filtered = f_transform_shifted * mask

    # --- Step 4: Apply Inverse Fourier Transform ---
    # Shift the zero-frequency component back to the top-left
    f_ishift = np.fft.ifftshift(f_transform_shifted_filtered)

    # Compute the Inverse DFT
    img_back = np.fft.ifft2(f_ishift)

    # Take the real part (or magnitude) and normalize for display
    img_back = np.abs(img_back)
    # Normalize to 0-255 and convert to uint8
    # filtered_image_spatial = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    # A simpler normalization if values are mostly positive after np.abs()
    if np.max(img_back) > 0:  # Avoid division by zero if image is all black
        filtered_image_spatial = (img_back / np.max(img_back) * 255).astype(np.uint8)
    else:
        filtered_image_spatial = np.zeros_like(img_back, dtype=np.uint8)

    print(f"Applied Fourier Transform and Low-Pass Filter to '{IMAGE_PATH}'. Displaying results...")

    # --- Display results using Matplotlib ---
    plt.figure(figsize=(12, 10))

    plt.subplot(2, 2, 1)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Original Grayscale Image')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Magnitude Spectrum (Log Scale)')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(mask, cmap='gray')
    plt.title(f'Low-Pass Filter Mask (Radius: {radius})')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.imshow(filtered_image_spatial, cmap='gray')
    plt.title('Image after LPF & Inverse DFT')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

except FileNotFoundError as fnf_error:
    print(fnf_error)
except Exception as e:
    import traceback

    print(f"An unexpected error occurred: {e}")
    traceback.print_exc()