from load_image import ft_load
from PIL import Image
import numpy as np

def zoom(image: Image.Image, factor: int):
    """
    Accepts an image and a zoom factor.
    Returns a new image that is zoomed by the factor.
    """
    new_image = image.resize((image.size[0] * factor, image.size[1] * factor))
    return new_image

def mode_to_channels(mode: str) -> int:
    """
    Accepts an image mode and returns the number of channels.
    """
    if mode == "1" or mode == "L":
        return 1
    elif mode == "RGB" or mode == "YCbCr" or mode == "LAB" or mode == "HSV":
        return 3
    elif mode == "RGBA" or mode == "CMYK":
        return 4
    else:
        return 0

def main():
    """
    Handles error cases and and run ft_load and zoom.
    """
    try:
        old_image = ft_load("./animal.jpeg")
        new_image = zoom(old_image, 10)
        image_shape = [new_image.size[1], new_image.size[0], mode_to_channels(new_image.mode)]
        print(f"New shape after slicing: {image_shape}")
        if new_image.mode != 'RGB':
            new_image = new_image.convert('RGB')
        all_pixels = []
        for pixel in new_image.getdata():
            all_pixels.append(list(pixel))
        array = np.array(all_pixels)
        print(array)
        new_image.show()
    except Exception as e:
        print(e)
    


if __name__ == "__main__":
    main()

