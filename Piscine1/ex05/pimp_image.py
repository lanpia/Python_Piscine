from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def ft_invert(image: np.ndarray) -> np.ndarray:
    """Invert the colors of the image"""
    return 255 - image

def ft_red(image: np.ndarray) -> np.ndarray:
    """Red Filter"""
    red_filter = image.copy()
    red_filter[:, :, 1:] = 0
    return red_filter

def ft_green(image: np.ndarray) -> np.ndarray:
    """Green Filter"""
    green_filter = image.copy()
    green_filter[:, :, [0, 2]] = 0
    return green_filter

def ft_blue(image: np.ndarray) -> np.ndarray:
    """Blue Filter"""
    blue_filter = image.copy()
    blue_filter[:, :, :2] = 0
    return blue_filter

def ft_grey(image: np.ndarray) -> np.ndarray:
    """Greyscale Filter"""
    grey_values = image.mean(axis=2, keepdims=True).astype(np.uint8)
    grey_filter = np.repeat(grey_values, 3, axis=2)
    return grey_filter

def main():
    image = Image.open("../landscape.jpeg")
    image_array = np.array(image)
    filters = [
        (image_array, "Original"),
        (ft_invert(image_array), "Inverted Colors"),
        (ft_red(image_array), "Red Filter"),
        (ft_green(image_array), "Green Filter"),
        (ft_blue(image_array), "Blue Filter"),
        (ft_grey(image_array), "Greyscale Filter")
    ]
    fig, axes = plt.subplots(3, 2, figsize=(12, 8))
    axes = axes.ravel()

    for ax, (filtered_image, title) in zip(axes, filters):
        ax.imshow(filtered_image)
        ax.set_title(title)
        ax.axis("off")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
    
	