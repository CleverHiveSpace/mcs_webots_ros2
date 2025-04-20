from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def image_to_elevation_grid(image_path, target_size=None, normalize=True, height_coefficient=1):
    """
    Convert a grayscale image to a list of elevation float values.

    Parameters:
    - image_path (str): Path to the grayscale image.
    - target_size (tuple): Resize image to (width, height). If None, use original size.
    - normalize (bool): If True, normalize pixel values to range [0.0, 1.0].

    Returns:
    - List of floats representing elevation.
    """
    # Open and convert to grayscale
    img = Image.open(image_path).convert('L')

    if target_size:
        img = img.resize(target_size, Image.LANCZOS)

    # Convert to NumPy array
    pixel_array = np.array(img, dtype=np.float32)

    if normalize:
        pixel_array /= 255.0  # Normalize to [0.0, 1.0]

    pixel_array *= height_coefficient

    return np.flipud(pixel_array).flatten().tolist()


# Example usage
if __name__ == "__main__":
    path = "../assets/moon_heightmap.png"
    target_size = (500, 500)
    height_coefficient = 10

    heights = image_to_elevation_grid(
        path, target_size=target_size, height_coefficient=height_coefficient)  # Resize to 10x10

    grid = np.array(heights).reshape(target_size)
    plt.imshow(grid)
    plt.show()

    for h in heights:
        print(round(h, 3), end=" ")
