import numpy as np
import array
from PIL import Image
# from numpy import array

def ft_load(path: str) -> array:
    """print the image_file"""
    try:
        image = Image.open(path)
        if image.format not in ["JPEG", "JPG"]:
            raise ValueError(f"Unsupported image format: {image.format}")
        image_array = np.array(image)
        print(f"The shape of image is: {image_array.shape}")
        
        return image_array

    except FileNotFoundError:
        print(f"Error: File not found at path '{path}'.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

