# roster.py

from PIL import Image
from enum import Enum


class LimbType(Enum):
    HEAD = 1
    ARM = 2
    LEG = 3
    TORSO = 4

# CLASSES.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class BackgroundImage:
    def __init__(self, filename, name, words):
        self.filename = filename
        self.words = words
        self.name = name


class SymbolImage:
    def __init__(self, filename, name, words):
        self.filename = filename
        self.words = words
        self.name = name


class Limb:
    def __init__(self, filename, name, words, joint):
        self.filename = filename
        self.words = words
        self.joint = joint
        self.name = name


class Subject:
    def __init__(self, filename, name, words):
        self.filename = filename
        self.words = words
        self.name = name

# THose are the classes.
# Now to define the OBJECTS themselves.

BG_LIST = [
    BackgroundImage(
        "bg_01.png",
        "Neptune",
        {
            "nouns": ["field", "tree", "sky", "wilderness"],
            "verbs": ["blow", "shine"]
        }
    ),
    BackgroundImage(
        "bg_02.png",
        "Path to Epic Mountain",
        {
            "nouns": ["lightning", "magic", "mountain", "true path", "pilgrimmage"],
            "verbs": ["ascend", "triumph", "despair", "walk"]
        }
    ),
    BackgroundImage(
        "bg_03.png",
        "Desert Highway",
        {
            "nouns": ["tower", "watcher", "warning", "beacon"],
            "verbs": ["warn", "hearald", "watch", "illuminate"]
        }
    ),
    BackgroundImage(
        "bg_04.png",
        "Surreal Office Labyrinth",
        {
            "nouns": ["maze", "trap", "corridor", "cubicle", "backroom"],
            "verbs": ["lose", "hide", "capture", "tangle", "confuse"]
        }
    ),
    BackgroundImage(
        "bg_05.png",
        "Picket Fence House",
        {
            "nouns": ["trash", "filth", "wasteland", "underbelly"],
            "verbs": ["decay", "discard", "reject"]
        }
    ),
    BackgroundImage(
        "bg_06.png",
        "Television Growing in Bushes",
        {
            "nouns": ["portal", "forest", "nightmare"],
            "verbs": ["trick", "mesmerize", "radiate"]
        }
    ),
    BackgroundImage(
        "bg_07.png",
        "Martian Desert",
        {
            "nouns": ["portal", "forest", "nightmare"],
            "verbs": ["trick", "mesmerize", "radiate"]
        }
    )

]


SYMBOL_LIST = [
    SymbolImage(
        "symbol_cup.png",
        "Coffee Mug",
        {
            "nouns": ["vessel", "basin", "chalice", "cup", "crucible", "liquid"],
            "verbs": ["hold", "carry", "protect", "deliver", "cherish", "contain"]
        }
    ),
    SymbolImage(
        "symbol_cross.png",
        "Old-style Bedazzled Crucifix",
        {
            "nouns": ["weapon", "hunter", "soldier", "killer", "battle"],
            "verbs": ["attack", "kill", "pursue", "destroy"]
        }
    ),
        SymbolImage(
        "symbol_keyboard.png",
        "Numpad Keyboard",
        {
            "nouns": ["panel","interface", "instrument", "heart"],
            "verbs": ["play", "create", "calculate", "think", "express", "input"]
        }
    ),
        SymbolImage(
        "symbol_pentacle.png",
        "Pentagram",
        {
            "nouns": ["altar", "pentacle", "devil"],
            "verbs": ["rejoice", "ravish", "ascend", "purchase"]
        }
    ),
        SymbolImage(
        "symbol_skull.png",
        "Chrome Skull",
        {
            "nouns": ["skull", "robot", "death", "space", "future"],
            "verbs": ["evolve", "create", "transcend", "consume"]
        }
    ),
    SymbolImage(
        "symbol_wrench.png",
        "Wrench",
        {
            "nouns": ["skull", "robot", "death", "space", "future"],
            "verbs": ["evolve", "create", "transcend", "consume"]
        }
    ),
        SymbolImage(
        "symbol_gun.png",
        "Pistol",
        {
            "nouns": ["skull", "robot", "death", "space", "future"],
            "verbs": ["evolve", "create", "transcend", "consume"]
        }
    ),
    SymbolImage(
        "symbol_germ.png",
        "Microbe",
        {
            "nouns": ["skull", "robot", "death", "space", "future"],
            "verbs": ["evolve", "create", "transcend", "consume"]
        }
    )


]


SUBJECT_LIST = [
    Subject(
        "subject_mulder.png",
        "Fox 'Spooky' Mulder",
        {}
    ),
    Subject(
        "subject_scully.png",
        "Dr. Dana Scully",
        {}
    ),
    Subject(
        "subject_strung_out.png",
        "Strung-out Wojak",
        {}
    ),
    Subject(
        "subject_wifejak.png",
        "Wifejak",
        {}
    ),

]
