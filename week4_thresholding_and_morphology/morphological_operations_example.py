import cv2  # OpenCV for image loading and morphological operations
import numpy as np
import matplotlib.pyplot as plt

# Path to your image file.
IMAGE_PATH = "sample_images/foto1.jpeg"  # Or choose another image

try:
    # Load the image in grayscale
    gray_image = cv2.imread(IMAGE_PATH, 0)

    if gray_image is None:
        raise FileNotFoundError(f"Image at path '{IMAGE_PATH}' not found or could not be opened.")

    # --- Binarize the image using Otsu's thresholding to get a binary image ---
    # Morphological operations are often applied to binary images.
    ret_otsu, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    print(f"Binarized the image using Otsu's threshold: {ret_otsu}")

    # --- Define a structuring element (kernel) ---
    # This kernel defines the neighborhood for the morphological operation.
    # A 5x5 square kernel is common. You can experiment with other shapes and sizes.
    # cv2.getStructuringElement(shape, ksize)
    # Shapes: cv2.MORPH_RECT, cv2.MORPH_ELLIPSE, cv2.MORPH_CROSS
    kernel_size = 5
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    # For some operations like Dilation/Erosion, a simple NumPy array can also be used:
    # kernel_np = np.ones((5,5), np.uint8)

    # --- Apply Morphological Operations ---

    # 1. Erosion
    # Erodes away the boundaries of foreground objects.
    # Useful for removing small white noises or disconnecting two connected objects.
    eroded_image = cv2.erode(binary_image, kernel, iterations=1)

    # 2. Dilation
    # Expands the boundaries of foreground objects.
    # Useful for filling small holes within objects or connecting disjoint objects.
    dilated_image = cv2.dilate(binary_image, kernel, iterations=1)

    # 3. Opening
    # An erosion followed by a dilation.
    # Useful for removing small objects (salt noise) while preserving the shape and size of larger objects.
    opened_image = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel, iterations=1)

    # 4. Closing
    # A dilation followed by an erosion.
    # Useful for closing small holes inside foreground objects or small black points on the object.
    closed_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel, iterations=1)

    # (Optional) Other operations like Gradient, Top Hat, Black Hat can also be explored
    # morphological_gradient = cv2.morphologyEx(binary_image, cv2.MORPH_GRADIENT, kernel)
    # tophat_image = cv2.morphologyEx(binary_image, cv2.MORPH_TOPHAT, kernel)
    # blackhat_image = cv2.morphologyEx(binary_image, cv2.MORPH_BLACKHAT, kernel)

    print(f"Applied morphological operations to the binarized version of '{IMAGE_PATH}'.")

    # --- Display results using Matplotlib ---
    titles = [
        'Original Grayscale', 'Binarized (Otsu)',
        f'Eroded (Kernel {kernel_size}x{kernel_size})', f'Dilated (Kernel {kernel_size}x{kernel_size})',
        f'Opened (Kernel {kernel_size}x{kernel_size})', f'Closed (Kernel {kernel_size}x{kernel_size})'
    ]
    images_to_display = [
        gray_image, binary_image,
        eroded_image, dilated_image,
        opened_image, closed_image
    ]

    plt.figure(figsize=(15, 10))  # Adjust figure size

    for i in range(len(images_to_display)):
        plt.subplot(2, 3, i + 1)  # Arrange in 2 rows, 3 columns
        plt.imshow(images_to_display[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')

    # If you add more operations like gradient, tophat, blackhat, adjust subplot layout
    # e.g., plt.figure(figsize=(15,15)) and plt.subplot(3,3, i+1)

    plt.tight_layout()
    plt.show()

except FileNotFoundError as fnf_error:
    print(fnf_error)
except Exception as e:
    import traceback

    print(f"An unexpected error occurred: {e}")
    traceback.print_exc()