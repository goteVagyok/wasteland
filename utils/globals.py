import pygame as pg
from datetime import datetime
import os

pg.font.init()


class Globals:

    def __init__(self):
        self.DEBUG = True
        self.cwd = os.getcwd()
        self.texture_path = f"{self.cwd}/assets/"
        self.tile_width = 100
        self.tile_height = 100
        self.window_width = 800
        self.window_height = 600
        self.dt: float  # undefined at start
        self.mono_font_size = 10
        self.mono_font = pg.font.Font("assets/textures/fonts/PixeloidMono.ttf", self.mono_font_size)

    def debug(self, msg):
        if self.DEBUG:
            time = datetime.now().strftime("%H:%M:%S")
            print(f"[{time}] {msg}")


class UIElementIds:

    player_inventory_id = 1


class Colors:
    black =         (40, 40, 40)
    light_black =   (60, 56, 54)

    red =           (204, 36, 29)
    light_red =     (251, 73, 52)

    green =         (152, 151, 26)
    light_green =   (184, 187, 38)

    yellow =        (215, 153, 33)
    light_yellow =  (250, 189, 47)

    blue =          (69, 133, 136)
    light_blue =    (131, 165, 152)

    magenta =       (177, 98, 134)
    light_magenta = (211, 134, 155)

    cyan =          (104, 157, 106)
    light_cyan =    (142, 192, 124)

    orange =        (215, 93, 14)
    light_orange =  (254, 128, 25)

    grey =          (143, 131, 116)
    light_grey =    (168, 153, 132)

    white =         (213, 195, 161)
    light_white =   (251, 241, 199)


def path_to_texture(path):
    return pg.image.load(path.value).convert_alpha()
