import numpy as np


def convert_to_text(image):
    w, h = image.size

    symbol_width = 7.2
    symbol_height = 18

    max_pixels = 140
    ratio = max_pixels/w

    resized_image = image.convert('LA').resize((int(w * ratio), int(h * ratio * ( symbol_width / symbol_height )))).convert("L")

    symbols = [" ", "-", "=", "O", "L", 'K', 'X']

    pixels = np.array(resized_image, dtype=np.int32)

    for i in range(len(symbols)):
        v = np.interp(len(symbols) - 1 - i, [0,len(symbols)], [0,255])
        pixels[pixels > v] = -(i)

    string = ""

    for x in range(pixels.shape[0]):
        for y in range(pixels.shape[1]):
            string += symbols[-pixels[x, y]]
        string += "\n"

    return string
