# tarot_gen.py

from PIL import Image
import os

def say_hi(name):
    bg_img = Image.open("tarot_gen/img/bg_01.png")
    symbol_img = Image.open("tarot_gen/img/symbol_skull.png")
    bg_img.paste(symbol_img, (0, 0), symbol_img)
    bg_img.save('result.png')


    return_string = "Hi, " + name + "!"
    return return_string


