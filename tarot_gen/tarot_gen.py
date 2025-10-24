# tarot_gen.py

from PIL import Image
import os
import io
import random

def say_hi(name):


    return_string = "Hi, " + name + "!"
    return return_string

# TO DO: pick a 

def get_bg():
    file_names = [
            "bg_01.png",
            "bg_02.png",
            "bg_03.png",
            "bg_04.png" ]
    random_index = random.randrange(0, len(file_names))
    filename_prefix = "tarot_gen/img/"
    full_filename = filename_prefix + file_names[random_index]
    bg_img = Image.open(full_filename)

    return bg_img

def get_img():
    bg_img = get_bg() # Image.open("tarot_gen/img/bg_01.png")
    symbol_img = Image.open("tarot_gen/img/symbol_skull.png")
    bg_img.paste(symbol_img, (0, 0), symbol_img)
    img_bytes = io.BytesIO() # THIS will be the image
    bg_img.save(img_bytes, format='PNG')
    img_bytes.seek(0) # reset stream position
    return img_bytes

