import pygame as pg
from datetime import datetime
import os


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

    def debug(self, msg):
        if self.DEBUG:
            time = datetime.now().strftime("%H:%M:%S")
            print(f"[{time}] {msg}")


def path_to_texture(path):
    return pg.image.load(path.value).convert_alpha()
