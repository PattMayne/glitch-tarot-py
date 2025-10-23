# tarot_gen.py

from PIL import Image
import os
import io

def say_hi(name):


    return_string = "Hi, " + name + "!"
    return return_string

def get_img():
    bg_img = Image.open("tarot_gen/img/bg_01.png")
    symbol_img = Image.open("tarot_gen/img/symbol_skull.png")
    bg_img.paste(symbol_img, (0, 0), symbol_img)
    img_bytes = io.BytesIO() # THIS will be the image
    bg_img.save(img_bytes, format='PNG')
    img_bytes.seek(0) # reset stream position
    return img_bytes

