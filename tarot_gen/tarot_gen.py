# tarot_gen.py

'''

    This script loads the component-images,
    pastes them onto the BG image,
    optionally performs some glitching,
    and returns the image.

    The image (card) can be returns as a PNG
    or as base64 data. PNG is when we need a file,
    base64 is when we want to embed the image directly
    into html (because there will be no saved file
    to link to).

    The functions that app.py might call are
    get_tarot_base64   AND   get_img
    Each delivers a single image.
    To get multiple images app.py must call the function
    multiple times.

    Image components are:
    - BG (background or world)
    - symbol (object)
    - subject (person or persona or perspective, psychological archetype or ccharacter)

    BG is the base image. It is drawn once.
    Symbol can be drawn multiple times, in a pattern, pasted on BG.
    Subject is drawn once
    A number is also drawn beside the subject, indicating the number of symbol-copies pasted
    Any of these elements can be glitched, except the number.
    Individual symbol-copies have a chance to be glitched or not-glitched.

    REVERSALS:
    There will be no card reversals in the image generation.
    The HTML display gives the dealer the option to allow randomized reversals.
    The discord bot is not likely to have reversals. But maybe we'll implement later.

    Glitching is done by manipulating the pixels of the image objects.

'''

from PIL import Image, ImageFont, ImageDraw
import os
import io
import random
from enum import Enum
import tarot_gen.img.roster as roster
import base64

SYMBOL_DIVISOR = 6
MAX_SYMBOLS = SYMBOL_DIVISOR - 1


def say_hi(name):
    return_string = "Hi, " + name + "!"
    return return_string


'''
Get one background image
@returns tuple (imagebytes, string, bool)
'''
def get_bg():
    bg_objects = roster.BG_LIST
    
    random_index = random.randrange(0, len(bg_objects))
    filename_prefix = "tarot_gen/img/"
    full_filename = filename_prefix + bg_objects[random_index].filename
    bg_name = bg_objects[random_index].name
    bg_img = Image.open(full_filename)
    bg_img = bg_img.resize((600, 900))

    chance_to_glitch = random.randint(0, 13)
    glitched = False
    if chance_to_glitch == 0:
        bg_img = glitch_image(bg_img)
        glitched = True

    return (bg_img, bg_name, glitched)


# SYMBOLS are like SUITS
def get_symbol():
    symbol_objects = roster.SYMBOL_LIST

    random_index = random.randrange(0, len(symbol_objects))
    filename_prefix = "tarot_gen/img/"
    full_filename = filename_prefix + symbol_objects[random_index].filename
    symbol_name = symbol_objects[random_index].name
    return (Image.open(full_filename), symbol_name)


# SUBJECTS personify it all. Connects the SYMBOL (object) to the WORLD (bg)
# @returns tuple (img_bytes, string, bool)
def get_subject():
    subject_objects = roster.SUBJECT_LIST
    random_index = random.randrange(0, len(subject_objects))
    filename_prefix = "tarot_gen/img/"
    full_filename = filename_prefix + subject_objects[random_index].filename
    name = subject_objects[random_index].name
    subject_img = Image.open(full_filename)

    # chance to glitch
    chance_to_glitch = random.randint(0, 12)
    glitched = False
    if chance_to_glitch == 0:
        subject_img = glitch_image(subject_img)
        glitched = True
    
    return (subject_img, name, glitched)



#  make a list of rows, where each row is represented
#  by the number (magnitude) of symbols to print.
#  and display the symbols with some elegance
# @params{ magnitude int }
# @return list[ int ]
def get_row_sizes(magnitude):
    list_of_row_sizes = [];

    # always add the max number allowed
    unassigned_spaces = magnitude + 0
    while unassigned_spaces > 0:
        spaces_this_row = MAX_SYMBOLS if unassigned_spaces >= MAX_SYMBOLS else unassigned_spaces
        list_of_row_sizes.append(spaces_this_row)
        unassigned_spaces = unassigned_spaces - spaces_this_row

    return list_of_row_sizes


# @return int
def get_distance_from_center(is_even, position, center):
    if is_even and position > center:
        #position -= 1
        center += 1
 
    diff = position - center
    if diff < 0:
        diff *= -1

    return diff


# the ENUM for how many patterns we have
class SymbolPatterns(Enum):
    FLAT = 1
    ARC = 2


# Decide which printing algorithm to use
# @return (int, int)
def print_symbols(bg_img, symbol_img, magnitude):

    pattern_enums = list(SymbolPatterns)
    pattern_enum = pattern_enums[int(random.randrange(0, len(pattern_enums)))]
    
    if pattern_enum == SymbolPatterns.ARC:
        return print_symbols_arc(bg_img, symbol_img, magnitude)
    elif pattern_enum == SymbolPatterns.FLAT:
        return print_symbols_flat(bg_img, symbol_img, magnitude)



# ALGORITHM for printing layers of arcs
# @return (int, int)
def print_symbols_arc(bg_img, symbol_img, magnitude):
    symbol_width, symbol_height = symbol_img.size
    y_symbol_index = 0
    arcing_y_adjustment = 0
    list_of_row_sizes = get_row_sizes(magnitude)

    bottom_row_y = 0
    glitches = 0

    # this row of symbols to print, where the "row" is a value 
    # which represents how many times to print symbol
    for symbols_in_this_row in list_of_row_sizes:
        # it must lower FIRST according to its distance from the center
        # but that must be ENHANCED by being lower in the rows
        # So START by getting the center - if it's even numbers, the first of the two center
        center_index = (symbols_in_this_row - int(symbols_in_this_row / 2)) - 1

        x_offset = (SYMBOL_DIVISOR - symbols_in_this_row) * symbol_width / 2
        is_even = symbols_in_this_row % 2 == 0
        quarter_symbol = int(symbol_width / 4)

        for symbol_index in range(symbols_in_this_row):
            distance_from_center = get_distance_from_center(is_even, symbol_index + 1, center_index + 1)
            arcing_y_adjustment = distance_from_center * quarter_symbol

            draw_x = int(x_offset + (symbol_index * symbol_width))
            draw_y = int((symbol_width / 2) + (y_symbol_index * (symbol_width + 10))) + arcing_y_adjustment
            bottom_row_y = draw_y + symbol_width

            img_to_draw = symbol_img
 
            # glitch or not 
            if random.randint(0, 15) == 0:
                img_to_draw = glitch_image(symbol_img)
                glitches += 1
            
            # finally actually draw the image
            bg_img.paste(img_to_draw, (draw_x, draw_y), img_to_draw)

        y_symbol_index += 1

    return (bottom_row_y, glitches)



# Print the specified number of symbols on the given bg_image
# there are multiple patterns / algorithms to randomly choose from
# @return (int, int)
def print_symbols_flat(bg_img, symbol_img, magnitude):
    symbol_width, symbol_height = symbol_img.size
    y_symbol_index = 0
    list_of_row_sizes = get_row_sizes(magnitude)
    vertical_flip = False
    header_space = int(symbol_width / 2)

    bottom_row_y = 0
    glitches = 0

    grid_height = int((bg_img.size[1] - (header_space * 2)) / symbol_width)

    for symbols_in_this_row in list_of_row_sizes:
        offset = (SYMBOL_DIVISOR - symbols_in_this_row) * symbol_width / 2

        for x_symbol_index in range(symbols_in_this_row):
            draw_x = int(offset + (x_symbol_index * symbol_width))
            draw_y = int(header_space + (y_symbol_index * (symbol_width)))

            if vertical_flip:
                draw_y = ((symbol_width * grid_height) - draw_y) - 1
            else:
                bottom_row_y = draw_y + symbol_width

            img_to_draw = symbol_img
 
            # glitch or not 
            if random.randint(0, 15) == 0:
                img_to_draw = glitch_image(symbol_img)
                glitches += 1
            
            # finally actually draw the image
            bg_img.paste(img_to_draw, (draw_x, draw_y), img_to_draw)

        if vertical_flip:
            y_symbol_index += 1
        vertical_flip = not vertical_flip

    bottom_row_y += int(symbol_width / 4)

    return (bottom_row_y, glitches)


# pastes the number (magnitude) of symbols drawn, alongside the subject image
def print_number_and_subject(bg_img, bottom_row_y, magnitude, symbol_width):
    # get subject
    subject_img, subject_name, subject_glitched = get_subject()
    bg_width, bg_height = bg_img.size

    bg_draw = ImageDraw.Draw(bg_img)

    filename_prefix = "tarot_gen/img/"
    full_filename = filename_prefix + "alte.ttf"

    font = ImageFont.truetype(full_filename, symbol_width)
    draw_x = int(symbol_width / 2)
    draw_y = int(bottom_row_y + (symbol_width / 2))
    bg_draw.text((draw_x, draw_y), str(magnitude), font=font)

    del bg_draw

    draw_x = int(bg_width / 2) - symbol_width
    subject_img = subject_img.resize((symbol_width * 2, symbol_width * 2))
    bg_img.paste(subject_img, (draw_x, bottom_row_y), subject_img)

    return (subject_name, subject_glitched)



# GLITCH EFFECTS

def split_glitch(img):
    width, height = img.size
    split_point_x = random.randint(10, width - 10)

    bg = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    pixels = img.load() # for manipulating particular pixels
    bg.paste(img, (split_point_x, 0), img)
    bg.paste(img, (split_point_x - width, 0), img)
    return bg



def glitch_image(og_img):

    # do a better selection method
    # maybe we need a glitch module
    if random.randint(0, 10) < 4:
        return split_glitch(og_img)

    img = og_img.copy()

    width, height = img.size
    pixels = img.load() # for manipulating particular pixels
    num_shifts = random.randint(3, 8)
    max_shift = int(height / 3)
    min_shift = int(height / 6)

    random_selector = random.randint(0, 2)
    shift_not_color = (random_selector == 0)

    # Doing a SHIFT glitch
    # will later add other glitches

    for _ in range(num_shifts):
        # Randomly choose a horizontal slice
        y_start = random.randint(5, height - 5)
        y_end = min(y_start + random.randint(min_shift, max_shift), height)
        shift_amount = random.randint(0, width)

        # Crop the slice
        box = (0, y_start, width, y_end)
        slice_img = img.crop(box)

        if shift_not_color:
            #return slice_img
            for y in range(y_start, y_end):
                for x in range(0, width):
                    pixels[x, y] = (0, 0, 0, 0)

            img.paste(slice_img, (shift_amount, y_start), slice_img)
            img.paste(slice_img, (shift_amount - width, y_start), slice_img)
        else:
            # changing color, not shift
            color_shift = random.randint(50, 150)

            for y in range(y_start, y_end):
                for x in range(0, width):
                    pixel_rgb = pixels[x, y]

                    r = (pixel_rgb[0] + color_shift) % 255
                    g = (pixel_rgb[1] + color_shift) % 255
                    b = (pixel_rgb[2] + color_shift) % 255

                    pixels[x, y] = (
                        r,
                        g,
                        b,
                        pixel_rgb[3]
                    )

    return img



#    FUNCTIONS FOR app.py



# To render raw onto the html page using jina template
# This is what we will USUALLY use.
def get_tarot_base64():
    img_tuple = get_img()

    # Encode as base64
    img_base64 = base64.b64encode(img_tuple[0].getvalue()).decode('utf-8')
    return (img_base64, img_tuple[1])


'''
    @Flask Route Function
    This is called from the router to get one image.
    ALL image requests come through here
    which therefore starts the chain of functions to generate
    a modular tarot card

    @returns tuple (imagebytes, alt_description_text)
'''
def get_img():

    # First get bg and symbol

    bg_img, bg_name, bg_glitched = get_bg() # Image.open("tarot_gen/img/bg_01.png")
    symbol_img, symbol_name = get_symbol() # Image.open("tarot_gen/img/symbol_skull.png")

    # We have the bg and symbol. Now find the correct size for the symbol
    # must therefore find how many (magnitude) symbols to draw

    magnitude = random.randrange(1, 25)
    img_size = bg_img.size
    bg_width, bg_height = img_size
    symbol_width = int(bg_width / SYMBOL_DIVISOR)
    symbol_img = symbol_img.resize((symbol_width, symbol_width))

    # We got all the data and elements we need. Print the symbols on the card.
    # we have multiple algorithms for how to display the symbols.
    bottom_row_y, symbol_glitch_count = print_symbols(bg_img, symbol_img, magnitude)

    # bottom_row_y is where we can print the number and subject

    subject_name, subject_glitched = print_number_and_subject(bg_img, bottom_row_y, magnitude, symbol_width)

    img_bytes = io.BytesIO() # THIS will be the image
    bg_img.save(img_bytes, format='PNG')
    img_bytes.seek(0) # reset stream position

    # build the alt description from names and glitch counts
    alt_desc_string = subject_name

    if subject_glitched:
        alt_desc_string += " (glitched)"

    alt_desc_string += " in " + bg_name

    if bg_glitched:
        alt_desc_string += " (glitched)"

    alt_desc_string += " with " + str(magnitude) + " " + symbol_name

    if magnitude > 1:
        alt_desc_string += "s"
    
    if symbol_glitch_count > 0:
        alt_desc_string += " (" + str(symbol_glitch_count) + " glitched)"

    return (img_bytes, alt_desc_string)


