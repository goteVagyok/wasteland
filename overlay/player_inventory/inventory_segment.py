import pygame as pg

from assets.texture_enum.textures import Textures
from items.item import Item
from overlay.overlay import OverlayComponent
from utils.globals import Globals, path_to_texture, Colors

Globals = Globals()


class InventorySegment(OverlayComponent):

    def __init__(self):
        super().__init__(0, 0, Textures.INVENTORY_SEGMENT)
        self.container: list[Item] = []
        self.normal_texture = path_to_texture(Textures.INVENTORY_SEGMENT)
        self.highlighted_texture = path_to_texture(Textures.INVENTORY_SEGMENT_HIGHLIGHTED)
        self.has_item = False
        self.num_of_items = 0
        self.num_of_items_font = Globals.mono_font.render(str(self.num_of_items), 0, Colors.black)
        self.num_of_items_pos = (0, 0)

    def highlight_segment_background(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.texture = self.highlighted_texture
        else:
            self.texture = self.normal_texture

    def add_item(self, item: Item):
        # center the item in the segment
        item.x = self.x + ((self.rect.w - item.rect.w) / 2)
        item.y = self.y + ((self.rect.h - item.rect.h) / 2)
        item.rect.x = item.x
        item.rect.y = item.y

        self.container.append(item)
        Globals.debug(f"item added: {item}")
        self.has_item = True
        self.num_of_items += 1
        self.num_of_items_font = Globals.mono_font.render(str(self.num_of_items), 0, Colors.black)

    def draw(self, screen):
        self.highlight_segment_background()
        screen.blit(self.texture, self.rect)

        if self.num_of_items > 0:
            self.container[0].draw(screen)
            screen.blit(self.num_of_items_font, self.num_of_items_pos)
