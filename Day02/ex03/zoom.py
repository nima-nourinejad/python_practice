from load_image import ft_load
from PIL import Image, ImageDraw, ImageFont
import numpy as np


def add_scale_and_size(image):
    """
    Adds scale and size text to the bottom left corner of the image.
    """
    font_size = 12
    font_color = (0, 0, 0)
    font = ImageFont.truetype("arial.ttf", font_size)
    draw = ImageDraw.Draw(image)
    scale_length = 50
    for i in range(50, image.width - 50, scale_length):
        draw.line([(i, image.height - 50), (i, image.height - 40)], fill=font_color)
        draw.text((i, image.height - 25), str(i - 50), font=font, fill=font_color)
    for i in range(50, image.height - 50, scale_length):
        draw.line([(40, i), (50, i)], fill=font_color)
        draw.text((15, i), str(i - 50), font=font, fill=font_color)
    image.show()

def zoom(image: Image.Image, factor: int):
    """
    Accepts an image and a zoom factor.
    Returns a new image that is zoomed by the factor.
    """
    new_size = [int(image.size[0] * factor), int(image.size[1] * factor)]
    new_image = image.resize(new_size)
    sliced_image = new_image.crop((0, 0, 400, 400))
    sliced_image = sliced_image.convert('L')
    image_shape = (400, 400, mode_to_channels(sliced_image.mode))
    print(f"New shape after slicing: {image_shape} or (400, 400)")
    all_pixels = []
    for pixel in sliced_image.getdata():
        temp = []
        temp.append(pixel)
        all_pixels.append(temp)
    array = np.array(all_pixels)
    print(array)
    new_width = 500
    new_height = 500
    extended_image = Image.new("RGB", (new_width, new_height), color=(255, 255, 255))
    extended_image.paste(sliced_image, (50, 50)) 
    add_scale_and_size(extended_image)


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
        zoom(old_image, 2)
    except Exception as e:
        print(e)
    


if __name__ == "__main__":
    main()

