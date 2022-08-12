import pygame as pg

from assets.texture_enum.textures import Textures
from items.item import Item
from overlay.overlay import OverlayComponent


class InventorySegment(OverlayComponent):

    def __init__(self):
        super().__init__(100, 100, Textures.INVENTORY_SEGMENT)
        self.container: list[Item] = []

    def highlight_segment_background(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.texture = Textures.INVENTORY_SEGMENT_HIGHLIGHTED
        else:
            self.texture = Textures.INVENTORY_SEGMENT

    @staticmethod
    def handle_mouse_event(self, event: pg.event):
        if event.type == pg.MOUSEBUTTONDOWN:
            pass

    def add_item(self, item: Item):
        # TODO center the item in the segment
        # item.x =
        # item.y =
        # item.rect.x =
        # item.rect.y =
        self.container.append(item)

    def draw(self, screen):
        screen.blit(self.texture, self.rect)
        for item in self.container:
            item.draw(screen)
