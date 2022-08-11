import pygame as pg

from assets.texture_enum.textures import Textures
from overlay.overlay import OverlayComponent


class Inventory(OverlayComponent):

    def __init__(self, container: list):
        super().__init__(100, 100, Textures.INVENTORY_SEGMENT)

        self.container = container
        self.slots = len(self.container)

        # TODO make inventory a collection of inv. segments (separate class). each segment should display its item
        #  and the number of them or smth. like that


    def draw(self, screen):
        for item in self.container:
            pass



