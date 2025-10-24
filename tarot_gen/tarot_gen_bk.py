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


# SYMBOLS are like SUITS, or identities
# 

def get_symbol():
    file_names = [
            "symbol_keyboard.png",
            "symbol_pentacle.png",
            "symbol_skull.png",
            "symbol_gun.png",
            "symbol_cup.png" ]
    random_index = random.randrange(0, len(file_names))
    filename_prefix = "tarot_gen/img/"
    full_filename = filename_prefix + file_names[random_index]
    return Image.open(full_filename)


#     I WANT TO USE THIS
#   to get a list of rows and row lengths
#  and display the symbols with some elegance
def get_row_sizes(magnitude):
    list_of_row_sizes = [1];
    if magnitude < 3:
        return list_of_row_sizes

    unassigned_spaces = magnitude + 0
    while unassigned_spaces > 0:
        max_spaces = 5 if unassigned_spaces > 4 else unassigned_spaces
        spaces_this_row = random.randrange(1, max_spaces)
        list_of_row_sizes.append(spaces_this_row)
        unassigned_spaces = unassigned_spaces - spaces_this_row

    return list_of_row_sizes



def get_img():
    bg_img = get_bg() # Image.open("tarot_gen/img/bg_01.png")
    symbol_img = get_symbol() # Image.open("tarot_gen/img/symbol_skull.png")

    # We have the bg and symbol. Now find the correct size for the symbol
    # must therefore find how many to draw

    magnitude = random.randrange(1, 12)
    img_size = bg_img.size
    bg_width, bg_height = img_size
    symbol_width = int(bg_width / 5)
    symbol_img = symbol_img.resize((symbol_width, symbol_width))
    
    draw_y = 25
    spaces = 0
    for i in range(magnitude):
        spaces = spaces + 1
        if spaces > 4:
            spaces = 0
            draw_y = draw_y + symbol_width
        draw_x = 25 + (spaces * symbol_width)
        bg_img.paste(symbol_img, (draw_x, draw_y), symbol_img)

    # we can have multiple algorithms for how to display the symbols.

    img_bytes = io.BytesIO() # THIS will be the image
    bg_img.save(img_bytes, format='PNG')
    img_bytes.seek(0) # reset stream position
    return img_bytes

