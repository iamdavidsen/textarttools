import numpy as np
from pyfiglet import Figlet


def convert_to_text(image, max_pixels, symbol_width, symbol_height, symbols):
    w, h = image.size

    #symbol_width = 7.2
    #symbol_height = 18

    #max_pixels = 200

    ratio = max_pixels/w

    resized_image = image.convert("L").resize((int(w * ratio), int(h * ratio * ( symbol_width / symbol_height ))))

    symbols =  symbols[::-1]

    pixels = np.array(resized_image, dtype=np.int32)

    pixels[pixels == 0] = 1
    for i in range(len(symbols)):
        v = np.interp(len(symbols) - 1 - i, [0,len(symbols)], [0,255])
        pixels[pixels > v] = -(i)

    string = ""

    for x in range(pixels.shape[0]):
        for y in range(pixels.shape[1]):
            string += symbols[-pixels[x, y]]
        string += "\n"

    return string

def convert_to_banner(text, width):
    fonts = ["banner", "big", "block", "bubble", "lean", "mini", "script", "shadow", "slant", "standard"]

    for i in range(len(fonts)):
        figlet = Figlet(font=fonts[i], width=width)
        fonts[i] = {"text": figlet.renderText(text), "font": fonts[i]}

    return fonts

