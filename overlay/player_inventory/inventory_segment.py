import pygame as pg

from assets.texture_enum.textures import Textures
from items.item import Item
from overlay.overlay import OverlayComponent
from utils.globals import Globals, path_to_texture

Globals = Globals()


class InventorySegment(OverlayComponent):

    def __init__(self):
        super().__init__(100, 100, Textures.INVENTORY_SEGMENT)
        self.container: list[Item] = []
        self.normal_texture = path_to_texture(Textures.INVENTORY_SEGMENT)
        self.highlighted_texture = path_to_texture(Textures.INVENTORY_SEGMENT_HIGHLIGHTED)

    def highlight_segment_background(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.texture = self.highlighted_texture
        else:
            self.texture = self.normal_texture

    @staticmethod
    def handle_mouse_event(self, event: pg.event):
        if event.type == pg.MOUSEBUTTONDOWN:
            pass

    def add_item(self, item: Item):
        # center the item in the segment
        item.x = self.x + ((self.rect.w - item.rect.w) / 2)
        item.y = self.y + ((self.rect.h - item.rect.h) / 2)
        item.rect.x = item.x
        item.rect.y = item.y

        self.container.append(item)

    def draw(self, screen):
        self.highlight_segment_background()
        screen.blit(self.texture, self.rect)
        for item in self.container:
            item.draw(screen)
