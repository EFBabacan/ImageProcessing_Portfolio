from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


def affine_transform_image(image_pil, scale=(1.0, 1.0), shear_params=(0.0, 0.0), angle_deg=0.0, translate=(0.0, 0.0),
                           mirror_scale=(1.0, 1.0)):
    """
    Applies a sequence of affine transformations to a PIL Image.
    The transformation order is: Scale -> ShearX -> ShearY -> Rotate -> Mirror -> Translate.
    The resulting image is sized to fit all transformed pixels, with the top-left
    of the transformed content aligned with the top-left (0,0) of the output image.

    Args:
        image_pil (PIL.Image.Image): The input PIL Image object.
        scale (tuple): (sx, sy) scaling factors for x and y axes.
        shear_params (tuple): (kx, ky) shear factors. kx shears along x-axis, ky along y-axis.
                              Note: PIL's default affine transform uses a slightly different shear definition.
                              This implementation builds matrices according to common geometric interpretations.
        angle_deg (float): Counter-clockwise rotation angle in degrees.
        translate (tuple): (tx, ty) translation distances for x and y axes.
        mirror_scale (tuple): (ax, ay) mirroring factors. ax=-1 mirrors horizontally, ay=-1 vertically.

    Returns:
        PIL.Image.Image: The transformed PIL Image object.
    """
    k_x, k_y = shear_params
    tx, ty = translate
    ax, ay = mirror_scale
    theta_rad = np.deg2rad(angle_deg)  # Convert angle to radians
    sx, sy = scale

    # --- Constructing the forward transformation matrix M_forward ---
    # M_forward maps input (source) coordinates to output (destination) coordinates:
    # P_out = M_forward * P_in
    # Order of matrix multiplication (applied to point from right to left):
    # M_forward = T * Mirror * R * Sh_y * Sh_x * Sc

    # Scaling Matrix
    Sc_mat = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
    # ShearX Matrix (shears x-coordinate based on y)
    Sh_x_mat = np.array([[1, k_x, 0], [0, 1, 0], [0, 0, 1]])
    # ShearY Matrix (shears y-coordinate based on x)
    Sh_y_mat = np.array([[1, 0, 0], [k_y, 1, 0], [0, 0, 1]])
    # Standard Counter-Clockwise Rotation Matrix
    cos_t, sin_t = np.cos(theta_rad), np.sin(theta_rad)
    R_mat = np.array([[cos_t, -sin_t, 0], [sin_t, cos_t, 0], [0, 0, 1]])
    # Mirroring Matrix
    Mir_mat = np.array([[ax, 0, 0], [0, ay, 0], [0, 0, 1]])
    # Translation Matrix
    T_mat = np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])

    # Combine transformations: T * Mirror * R * Sh_y * Sh_x * Sc
    M_forward = T_mat @ Mir_mat @ R_mat @ Sh_y_mat @ Sh_x_mat @ Sc_mat

    # --- Calculate new image dimensions to fit the transformed image ---
    w, h = image_pil.size
    # Original corners in homogeneous coordinates (x, y, 1)
    # Points: (0,0), (w-1,0), (0,h-1), (w-1,h-1)
    corners = np.array([
        [0, w - 1, 0, w - 1],
        [0, 0, h - 1, h - 1],
        [1, 1, 1, 1]
    ])

    transformed_corners = M_forward @ corners

    min_x_coord = np.min(transformed_corners[0, :])
    max_x_coord = np.max(transformed_corners[0, :])
    min_y_coord = np.min(transformed_corners[1, :])
    max_y_coord = np.max(transformed_corners[1, :])

    new_width = int(np.round(max_x_coord - min_x_coord))
    new_height = int(np.round(max_y_coord - min_y_coord))

    if new_width <= 0 or new_height <= 0:
        print(f"Warning: Calculated new image dimensions are non-positive ({new_width}x{new_height}). "
              "This can happen with extreme mirror/scale parameters. Returning original image.")
        return image_pil

    # --- Prepare matrix for PIL.Image.transform ---
    # PIL's transform method requires the *inverse* of the forward affine transformation matrix.
    # This inverse matrix maps coordinates from the destination image back to the source image.
    # P_in = M_inverse * P_out
    # Additionally, we need to adjust the translation so the transformed image's
    # top-left bounding box corner is at (0,0) in the output image canvas.

    # This matrix translates the content in the transformed coordinate system
    # so that its new bounding box's top-left corner moves to (0,0).
    T_adjust_origin = np.array([
        [1, 0, -min_x_coord],
        [0, 1, -min_y_coord],
        [0, 0, 1]
    ])

    # Final forward matrix that maps source to the new canvas (where content starts at 0,0)
    M_final_forward_to_canvas = T_adjust_origin @ M_forward

    try:
        M_inverse_for_pil = np.linalg.inv(M_final_forward_to_canvas)
    except np.linalg.LinAlgError:
        print("Error: Final matrix for PIL is not invertible. Check transformation parameters.")
        return image_pil  # Return original image if matrix is singular

    # PIL expects a 6-tuple (a, b, c, d, e, f) from the inverse matrix:
    # where (a,b,c) is the first row and (d,e,f) is the second row of the 3x3 matrix,
    # representing the affine part of M_inverse_for_pil.
    # x_src = a*x_dst + b*y_dst + c
    # y_src = d*x_dst + e*y_dst + f
    pil_coeffs = (
        M_inverse_for_pil[0, 0], M_inverse_for_pil[0, 1], M_inverse_for_pil[0, 2],
        M_inverse_for_pil[1, 0], M_inverse_for_pil[1, 1], M_inverse_for_pil[1, 2]
    )

    # Apply the transformation using PIL
    transformed_image = image_pil.transform(
        (new_width, new_height),  # Output size
        Image.AFFINE,  # Transformation type
        pil_coeffs,  # The 6 coefficients of the inverse matrix
        resample=Image.BICUBIC  # Resampling filter for better quality
    )
    return transformed_image


if __name__ == '__main__':
    # Path to your image file.
    # Make sure "foto1.jpeg" is in the same directory as this script,
    # or provide the correct full or relative path.
    IMAGE_PATH = "foto1.jpeg"
    try:
        original_image = Image.open(IMAGE_PATH)

        # Example transformation parameters (you can change these)
        # These are similar to those used in the PDF example on page 17
        transformed_img = affine_transform_image(
            original_image,
            scale=(1.2, 1.2),  # Scale up by 20%
            shear_params=(0.0, 0.0),  # No shear in this example (PDF page 17 uses (0.0, 0.0) for 'kayma r')
            angle_deg=45.0,  # Rotate 45 degrees counter-clockwise (PDF uses pi/4)
            translate=(10.0, 0.0),  # Translate 10 pixels right (PDF uses (10,0))
            mirror_scale=(-1.0, -1.0)  # Mirror on both axes (PDF uses (-1,-1))
        )

        # Display the original and transformed images
        plt.figure(figsize=(12, 6))  # Adjust figure size as needed

        plt.subplot(1, 2, 1)
        plt.imshow(original_image)
        plt.title(f"Original Image: {IMAGE_PATH}")
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.imshow(transformed_img)
        plt.title("Affine Transformed Image")
        plt.axis('off')

        plt.tight_layout()  # Adjusts subplot params for a tight layout.
        plt.show()

    except FileNotFoundError:
        print(f"Error: The file '{IMAGE_PATH}' was not found. Please check the file path.")
    except Exception as e:
        import traceback

        print(f"An unexpected error occurred: {e}")
        print("--- Traceback ---")
        traceback.print_exc()
        print("-----------------")