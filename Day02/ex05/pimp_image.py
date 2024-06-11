from load_image import ft_load
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def ft_invert(array):
    max_values_columns = np.max(array, axis=0)
    image = Image.new("RGB", ((max_values_columns[1] - 255), (max_values_columns[0] -255)))
    lst = array.tolist()
    i = 0
    while i < len(lst):
        loc = ((lst[i][1] - 256), (lst[i][0] - 256))
        raw_data = lst[i + 1]
        raw_data_array = np.array(raw_data)
        data_array = 255 - raw_data_array
        data = data_array.tolist()
        data = tuple(data)
        image.putpixel(loc, data)
        i += 2
    image.show()
