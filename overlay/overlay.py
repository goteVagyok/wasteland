import pygame as pg

from sprite.sprite import Sprite
from utils.globals import Globals

Globals = Globals()


class OverlayComponent(Sprite):

    def __init__(self, x, y, texture):
        super().__init__(texture, x, y, False)
        self.x = x
        self.y = y

        self.shown = False

    def toggle_shown(self, event, hotkey):
        if event.type == pg.KEYDOWN:
            if event.key == hotkey:
                self.shown = not self.shown

    def show_component(self, event, hotkey, screen):
        self.toggle_shown(event, hotkey)
        if self.shown:
            self.draw(screen)
