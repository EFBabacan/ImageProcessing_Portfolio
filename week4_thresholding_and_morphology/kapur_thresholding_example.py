import cv2  # OpenCV for image loading
import numpy as np
import matplotlib.pyplot as plt

# skimage.filters'dan threshold_kapur'u import etmeye çalışacağız
# Eğer ModuleNotFoundError alırsanız, 'pip install scikit-image' komutunu terminalde çalıştırın.
try:
    from skimage.filters import threshold_kapur
except ModuleNotFoundError:
    print("Error: The scikit-image library is not installed, or threshold_kapur could not be imported.")
    print("Please install it by running: pip install scikit-image")
    print("If already installed, ensure your Python environment is correctly configured in PyCharm.")
    exit()  # Exit the script if skimage is not available

# Path to your image file within the sample_images subfolder of week4.
# Make sure to create 'week4_thresholding_and_morphology/sample_images/'
# and place your image there.
IMAGE_PATH = "sample_images/foto1.jpeg"  # Or choose an image that might be bimodal

try:
    # Load the image in grayscale
    gray_image = cv2.imread(IMAGE_PATH, 0)

    if gray_image is None:
        raise FileNotFoundError(f"Image not found or could not be opened: {IMAGE_PATH}")

    # --- Apply Kapur's Entropy Thresholding using scikit-image ---
    # threshold_kapur function returns the optimal threshold value.
    thresh_kapur_val = threshold_kapur(gray_image)

    # Binarize the image using the threshold found by Kapur's method
    # Pixels > threshold become True, else False.
    # For display, convert boolean array to uint8 (0 or 255).
    binary_image_kapur = (gray_image > thresh_kapur_val).astype(np.uint8) * 255

    print(f"Applied Kapur's entropy thresholding to '{IMAGE_PATH}'.")
    print(f"Optimal threshold value found by Kapur's method: {thresh_kapur_val}")

    # --- Display results using Matplotlib ---
    plt.figure(figsize=(18, 6))  # Adjusted figure size for better layout

    # 1. Original Grayscale Image
    plt.subplot(1, 3, 1)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Original Grayscale Image')
    plt.axis('off')

    # 2. Histogram of the Grayscale Image & Kapur's Threshold
    plt.subplot(1, 3, 2)
    plt.hist(gray_image.ravel(), bins=256, range=[0, 256], color='gray', alpha=0.75)
    plt.axvline(thresh_kapur_val, color='red', linestyle='dashed', linewidth=2,
                label=f'Kapur Threshold: {thresh_kapur_val:.2f}')  # Using .2f for float display
    plt.title('Grayscale Histogram & Kapur\'s Threshold')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency (Number of Pixels)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)

    # 3. Kapur's Thresholded Image
    plt.subplot(1, 3, 3)
    plt.imshow(binary_image_kapur, cmap='gray')
    plt.title(f'Kapur\'s Binarization (Thresh={thresh_kapur_val:.2f})')  # Using .2f for float display
    plt.axis('off')

    plt.tight_layout()
    plt.show()

except ModuleNotFoundError:
    # This specific except block for ModuleNotFoundError related to skimage was added
    # based on the assumption that the first try-except for skimage import might not catch all scenarios
    # if the script proceeds further. However, the top-level try-except for skimage import should handle it.
    # Keeping this for robustness in case of other unexpected module issues, though less likely for this specific problem.
    print("A critical module was not found. Ensure all dependencies like scikit-image are installed.")
    print("Try running: pip install scikit-image opencv-python numpy matplotlib Pillow")
except FileNotFoundError as fnf_error:
    print(fnf_error)
except Exception as e:
    import traceback

    print(f"An unexpected error occurred: {e}")
    traceback.print_exc()