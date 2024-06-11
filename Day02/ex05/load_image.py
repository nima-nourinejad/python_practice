import numpy as np
from PIL import Image

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

def ft_load(path: str):
    """
     loads an image, prints its format, and its pixels
    content in RGB format.
    """
    image = Image.open(path)
    image.show()
    image_format = image.format
    image_shape = [image.size[1], image.size[0], mode_to_channels(image.mode)]
    if image.mode != 'RGB':
        image = image.convert('RGB')
    all_pixels = []
    for i in range(image_shape[0]):
        for j in range(image_shape[1]):
            all_pixels.append((i + 256, j + 256, 0))
            all_pixels.append(image.getpixel((j, i)))
    array = np.array(all_pixels)
    return array


def main(path: str):
    """
    Handles error cases and and run ft_load.
    """
    try:
        ft_load(path)
    except Exception as e:
        print(e)
    

if __name__ == "__main__":
    main()
