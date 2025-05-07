import numpy as np
from PIL import Image  # Make sure this import is active


# import matplotlib.pyplot as plt # Uncomment if you use the optional display part

def bilinear_interpolate(image_array, y_coord, x_coord):
    """
    Applies bilinear interpolation on a given image array (numpy array)
    for the specified x, y coordinates.

    Args:
        image_array (np.array): Grayscale image (2D array) or color (3D array).
                                If color, operations are done channel-wise.
        y_coord (float): The y-coordinate for interpolation.
        x_coord (float): The x-coordinate for interpolation.

    Returns:
        float or np.array: Interpolated pixel value(s).
                           A single float for grayscale, a 1D array (color channels) for color.
    """
    x = np.asarray(x_coord)
    y = np.asarray(y_coord)

    x0 = np.floor(x).astype(int)
    x1 = x0 + 1
    y0 = np.floor(y).astype(int)
    y1 = y0 + 1

    # Clip coordinates to be within image boundaries
    # image_array.shape[1] is width, image_array.shape[0] is height
    x0 = np.clip(x0, 0, image_array.shape[1] - 1)
    x1 = np.clip(x1, 0, image_array.shape[1] - 1)
    y0 = np.clip(y0, 0, image_array.shape[0] - 1)
    y1 = np.clip(y1, 0, image_array.shape[0] - 1)

    # Get neighboring pixels
    Ia = image_array[y0, x0]
    Ib = image_array[y1, x0]
    Ic = image_array[y0, x1]
    Id = image_array[y1, x1]

    # Calculate weights
    wa = (x1 - x) * (y1 - y)
    wb = (x1 - x) * (y - y0)
    wc = (x - x0) * (y1 - y)
    wd = (x - x0) * (y - y0)

    # For color images (e.g., (H, W, 3)), weights (H,W) need to be (H,W,1) for broadcasting
    if image_array.ndim == 3 and wa.ndim == 2:  # Ensure weights are broadcastable if image is color
        wa = wa[..., np.newaxis]
        wb = wb[..., np.newaxis]
        wc = wc[..., np.newaxis]
        wd = wd[..., np.newaxis]

    interpolated_value = wa * Ia + wb * Ib + wc * Ic + wd * Id
    return interpolated_value


if __name__ == '__main__':
    # Path to your image file.
    # Make sure "foto1.jpeg" is in the same directory as this script,
    # or provide the correct full or relative path.
    IMAGE_PATH = "foto1.jpeg"

    try:
        # Load the image using Pillow
        img_pil_color = Image.open(IMAGE_PATH)
        # Convert the Pillow image to a NumPy array (it will be an RGB color image if not grayscale)
        img_array_color = np.array(img_pil_color)

        # For a grayscale interpolation example, convert the color image to grayscale
        img_pil_gray = img_pil_color.convert("L")
        img_array_gray = np.array(img_pil_gray)  # NumPy array for grayscale version

        # Get image dimensions
        if img_array_color.ndim == 3:
            height, width, _ = img_array_color.shape
        else:
            height, width = img_array_color.shape

        print(f"Using image: '{IMAGE_PATH}' with dimensions (Height, Width): ({height}, {width})")

        # Let's choose some fractional coordinates based on your previous output
        y_test = 512.25
        x_test = 683.32

        # Check if coordinates are valid (within image boundaries, not on the very edge pixel for interpolation)
        if not (0 <= y_test < height - 1 and 0 <= x_test < width - 1):  # Allow y_test or x_test to be 0
            print(f"Warning: Test coordinates ({y_test:.2f}, {x_test:.2f}) might be problematic for interpolation "
                  f"if they are on the absolute edge or outside. The function will clip, but results might be less meaningful.")
            # For safety, adjust if they are at the very last pixel row/column or beyond for interpolation's x1, y1
            y_test = min(y_test, height - 1.001)  # ensure y1 is within bounds
            x_test = min(x_test, width - 1.001)  # ensure x1 is within bounds
            y_test = max(y_test, 0)
            x_test = max(x_test, 0)

        print(f"Test coordinates for interpolation (y, x): ({y_test:.2f}, {x_test:.2f})")

        # Perform bilinear interpolation on the grayscale image version
        interpolated_value_gray = bilinear_interpolate(img_array_gray, y_test, x_test)
        print(f"Interpolated GRAYSCALE pixel value at ({y_test:.2f}, {x_test:.2f}): {interpolated_value_gray:.2f}")

        # Perform bilinear interpolation on the original color image
        interpolated_value_color = bilinear_interpolate(img_array_color, y_test, x_test)
        if hasattr(interpolated_value_color, "__getitem__") and len(interpolated_value_color) == 3:
            print(f"Interpolated COLOR (RGB) pixel value at ({y_test:.2f}, {x_test:.2f}): "
                  f"[{interpolated_value_color[0]:.2f}, {interpolated_value_color[1]:.2f}, {interpolated_value_color[2]:.2f}]")
        else:
            print(
                f"Interpolated value (possibly from grayscale source) at ({y_test:.2f}, {x_test:.2f}): {interpolated_value_color:.2f}")

        # --- OPTIONAL: Display the image and the point using Matplotlib ---
        # If you want to see the image and where the point is, uncomment the following lines.
        # Make sure 'import matplotlib.pyplot as plt' is active at the top of the script.
        """
        import matplotlib.pyplot as plt
        plt.figure(figsize=(8, int(8 * height / width) if width > 0 else 6)) 
        plt.imshow(img_array_color) 
        plt.scatter(x_test, y_test, c='red', edgecolor='white', s=100, zorder=5, label=f'Point ({x_test:.1f}, {y_test:.1f})') 
        plt.title(f"Image: '{IMAGE_PATH}'")
        plt.xlabel("X-coordinate (width)")
        plt.ylabel("Y-coordinate (height)")
        plt.legend()
        plt.show()
        """

    except FileNotFoundError:
        print(f"Error: The file '{IMAGE_PATH}' was not found. Please check the file path.")
    except Exception as e:
        # Print the full error for debugging
        import traceback

        print(f"An unexpected error occurred: {e}")
        print("--- Traceback ---")
        traceback.print_exc()
        print("-----------------")