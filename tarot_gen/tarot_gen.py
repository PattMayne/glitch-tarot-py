# tarot_gen.py

from PIL import Image
import os
import io
import random
from enum import Enum

SYMBOL_DIVISOR = 6
MAX_SYMBOLS = SYMBOL_DIVISOR - 1

def say_hi(name):
    return_string = "Hi, " + name + "!"
    return return_string

# TO DO: pick a what?

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


#  make a list of rows, where each row is represented
#  by the number (magnitude) of symbols to print.
#  and display the symbols with some elegance
# @params{ magnitude int }
# @return list[ int ]
def get_row_sizes(magnitude):
    list_of_row_sizes = [];

    # if the magnitude is small enough, we only need one row
    if magnitude < 3:
        list_of_row_sizes.append(1)
        return list_of_row_sizes

    # remove ONE from magnitude
    # Because this one will be the BOTTOM row
    # (it is solo and will eventually be part of a modular creature)

    magnitude = magnitude - 1

    # always add the max number allowed
    unassigned_spaces = magnitude + 0
    while unassigned_spaces > 0:
        spaces_this_row = MAX_SYMBOLS if unassigned_spaces >= MAX_SYMBOLS else unassigned_spaces
        list_of_row_sizes.append(spaces_this_row)
        unassigned_spaces = unassigned_spaces - spaces_this_row

    # adding that 1 back on
    list_of_row_sizes.append(1)

    return list_of_row_sizes


# @return int
def get_distance_from_center(is_even, position, center):
    if is_even and position > center:
        #position -= 1
        center += 1
 
    diff = position - center
    if diff < 0:
        diff *= -1

    print(" ")
    print("DIFF:")
    print(diff)
    print(" ")

    return diff


# ALGORITHM for printing layers of arcs
def print_symbols_arc(bg_img, symbol_img, magnitude):
    print("doing arc")
    symbol_width, symbol_height = symbol_img.size
    y_symbol_index = 0
    arcing_y_adjustment = 0
    list_of_row_sizes = get_row_sizes(magnitude)

    # this row of symbols to print, where the "row" is a value 
    # which represents how many times to print symbol
    for symbols_in_this_row in list_of_row_sizes:
        #print(symbols_in_this_row)

        # it must lower FIRST according to its distance from the center
        # but that must be ENHANCED by being lower in the rows
        # So START by getting the center - if it's even numbers, the first of the two center
        center_index = (symbols_in_this_row - int(symbols_in_this_row / 2)) - 1

        #arcing_y_adjustment = int(arcing_y_adjustment + (y_symbol_index * (symbol_width / 4)) * 1.5)
        x_offset = (SYMBOL_DIVISOR - symbols_in_this_row) * symbol_width / 2
        is_even = symbols_in_this_row % 2 == 0
        quarter_symbol = int(symbol_width / 4)

        is_string = " is even " if is_even else " is NOT even"
        print("\nROW: center of ", symbols_in_this_row, " is ", center_index)
        print(symbols_in_this_row, is_string)

        for symbol_index in range(symbols_in_this_row):
            distance_from_center = get_distance_from_center(is_even, symbol_index + 1, center_index + 1)
            print(symbol_index, " is ", distance_from_center, " from ", center_index)
            # get
            arcing_y_adjustment = distance_from_center * quarter_symbol
                #0 if symbol_index == center_index || (is_even && symbol_index == center_index + 1) else

            draw_x = int(x_offset + (symbol_index * symbol_width))
            draw_y = int((symbol_width / 2) + (y_symbol_index * (symbol_width + 10))) + arcing_y_adjustment
            print('arcing y:', arcing_y_adjustment)
            # finally actually draw the image
            bg_img.paste(symbol_img, (draw_x, draw_y), symbol_img)

        y_symbol_index += 1



# the ENUM for how many patterns we have
class SymbolPatterns(Enum):
    FLAT = 1
    ARC = 2


# Decide which printing algorithm to use
def print_symbols(bg_img, symbol_img, magnitude):
    symbol_pattern_option = random.randrange(0, len(SymbolPatterns))

    pattern_enums = list(SymbolPatterns)
    pattern_enum = pattern_enums[int(random.randrange(0, len(pattern_enums)))]
    
    if pattern_enum == SymbolPatterns.ARC:
        print_symbols_arc(bg_img, symbol_img, magnitude)
    elif pattern_enum == SymbolPatterns.FLAT:
        print_symbols_flat(bg_img, symbol_img, magnitude)





def print_symbols_flat(bg_img, symbol_img, magnitude):
    print("doing flat")
    symbol_width, symbol_height = symbol_img.size
    y_symbol_index = 0
    list_of_row_sizes = get_row_sizes(magnitude)

    for symbols_in_this_row in list_of_row_sizes:
        print(symbols_in_this_row)

        offset = (SYMBOL_DIVISOR - symbols_in_this_row) * symbol_width / 2

        for symbol_index in range(symbols_in_this_row):
            draw_x = int(offset + (symbol_index * symbol_width))
            draw_y = int((symbol_width / 2) + (y_symbol_index * (symbol_width + 10)))
            # finally actually draw the image
            bg_img.paste(symbol_img, (draw_x, draw_y), symbol_img)

        y_symbol_index += 1



# The main function to get an image
# @returns raw image bytes
def get_img():
    bg_img = get_bg() # Image.open("tarot_gen/img/bg_01.png")
    symbol_img = get_symbol() # Image.open("tarot_gen/img/symbol_skull.png")

    # We have the bg and symbol. Now find the correct size for the symbol
    # must therefore find how many to draw

    magnitude = random.randrange(1, 14)
    img_size = bg_img.size
    bg_width, bg_height = img_size
    symbol_width = int(bg_width / SYMBOL_DIVISOR)
    symbol_img = symbol_img.resize((symbol_width, symbol_width))
    print(magnitude)

    print_symbols(bg_img, symbol_img, magnitude)

 # we can have multiple algorithms for how to display the symbols.

    img_bytes = io.BytesIO() # THIS will be the image
    bg_img.save(img_bytes, format='PNG')
    img_bytes.seek(0) # reset stream position
    return img_bytes

