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
    def __init__(self, filename, words):
        self.filename = filename
        self.words = words


class SymbolImage:
    def __init__(self, filename, words):
        self.filename = filename
        self.words = words


class Limb:
    def __init__(self, filename, words, joint):
        self.filename = filename
        self.words = words
        self.joint = joint


# THose are the classes.
# Now to define the OBJECTS themselves.

BG_LIST = [
    BackgroundImage(
        "bg_01.png",
        {
            "nouns": ["field", "tree", "sky", "wilderness"],
            "verbs": ["blow", "shine"]
        }
    ),
    BackgroundImage(
        "bg_02.png",
        {
            "nouns": ["lightning", "magic", "mountain", "true path", "pilgrimmage"],
            "verbs": ["ascend", "triumph", "despair", "walk"]
        }
    ),
    BackgroundImage(
        "bg_03.png",
        {
            "nouns": ["vehicle", "metro", "compartment", "network", "surface"],
            "verbs": ["streamline", "speed", "connect", "manifest"]
        }
    ),
    BackgroundImage(
        "bg_04.png",
        {
            "nouns": ["cathedral", "homage", "honor", "geometry"],
            "verbs": ["save", "pray", "worship", "create"]
        }
    ),
    BackgroundImage(
        "bg_05.png",
        {
            "nouns": ["tower", "watcher", "warning", "beacon"],
            "verbs": ["warn", "hearald", "watch", "illuminate"]
        }
    ),
    BackgroundImage(
        "bg_06.png",
        {
            "nouns": ["maze", "trap", "corridor", "cubicle", "backroom"],
            "verbs": ["lose", "hide", "capture", "tangle", "confuse"]
        }
    ),
    BackgroundImage(
        "bg_07.png",
        {
            "nouns": ["trash", "filth", "wasteland", "underbelly"],
            "verbs": ["decay", "discard", "reject"]
        }
    ),
    BackgroundImage(
        "bg_08.png",
        {
            "nouns": ["tree", "river", "forest", "life"],
            "verbs": ["live", "frolick", "nurture"]
        }
    ),
    BackgroundImage(
        "bg_09.png",
        {
            "nouns": ["portal", "forest", "nightmare"],
            "verbs": ["trick", "mesmerize", "radiate"]
        }
    )
]


SYMBOL_LIST = [
    SymbolImage(
        "symbol_cup.png",
        {
            "nouns": ["vessel", "basin", "chalice", "cup", "crucible", "liquid"],
            "verbs": ["hold", "carry", "protect", "deliver", "cherish", "contain"]
        }
    ),
    SymbolImage(
        "symbol_gun.png",
        {
            "nouns": ["weapon", "hunter", "soldier", "killer", "battle"],
            "verbs": ["attack", "kill", "pursue", "destroy"]
        }
    ),
        SymbolImage(
        "symbol_keyboard.png",
        {
            "nouns": ["panel","interface", "instrument", "heart"],
            "verbs": ["play", "create", "calculate", "think", "express", "input"]
        }
    ),
        SymbolImage(
        "symbol_pentacle.png",
        {
            "nouns": ["altar", "pentacle", "devil"],
            "verbs": ["rejoice", "ravish", "ascend", "purchase"]
        }
    ),
        SymbolImage(
        "symbol_skull.png",
        {
            "nouns": ["skull", "robot", "death", "space", "future"],
            "verbs": ["evolve", "create", "transcend", "consume"]
        }
    ),
]
