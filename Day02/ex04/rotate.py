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

def rotate(image: Image.Image, x: int, y: int, size: int):
    """
    Accepts an image and a zoom factor.
    Returns a new image that is zoomed by the factor.
    """
    sliced_image = image.crop((x, y, x + size, y + size))
    sliced_image = sliced_image.convert('L')
    print(f"The shape of image is: (400, 400, 1) or (400, 400)")
    all_pixels = []
    for pixel in sliced_image.getdata():
        temp = []
        temp.append(pixel)
        all_pixels.append(temp)
    array = np.array(all_pixels)
    print(array)
    sliced_image.show()
    rotated_image = Image.new("L", (400, 400))
    rotated_image.show()
    for i in range(400):
        for j in range(400):
            pixel_data = sliced_image.getpixel((i, j))
            rotated_image.putpixel((j, (399 - i)), pixel_data) 
    rotated_image.show()
    all_pixels = []
    print(f"New shape after Transpose: (400, 400)")
    for pixel in rotated_image.getdata():
        temp = []
        temp.append(pixel)
        all_pixels.append(temp)
    array = np.array(all_pixels)
    print(array)
    new_width = 500
    new_height = 500
    extended_image = Image.new("RGB", (new_width, new_height), color=(255, 255, 255))
    extended_image.paste(rotated_image, (50, 50)) 
    add_scale_and_size(extended_image)

def main():
    """
    Handles error cases and and run ft_load and zoom.
    """
    try:
        old_image = ft_load("./animal.jpeg")
        old_image.show()
        rotate(old_image, 450 ,100 , 400)
    except Exception as e:
        print(e)
    


if __name__ == "__main__":
    main()
