import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def zoom_image(image_array: np.ndarray, start_x: int, start_y: int, size: int) -> np.ndarray:
    """Zoom the image"""

    try:
        zoomed_array = image_array[start_x:start_x+size, start_y:start_y+size]
        zoomed_array = zoomed_array[...,:1]
        return zoomed_array
    except IndexError:
        print("Error: The slicing indices are out of bounds.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def drow_image(image_array: np.ndarray, title: str) -> None:
    """Draw the image"""

    plt.imshow(image_array)
    plt.title(title)
    plt.xticks(np.arange(0, image_array.shape[1], step=50))
    plt.yticks(np.arange(0, image_array.shape[0], step=50))
    plt.show()

def main():
    path = "../animal.jpeg"
    image_array = ft_load(path)
    if image_array is None:
        return
    print(f"The shape of image is: {image_array.shape}")
    print(image_array)

    zoomed_array = zoom_image(image_array, start_x=100, start_y=450, size=400)
    if zoomed_array is None:
        return
    print(f"New shape after slicing: {zoomed_array.shape}")
    print(zoomed_array)
    drow_image(zoomed_array, "Zoom Image")

if __name__ == "__main__":
    main()
