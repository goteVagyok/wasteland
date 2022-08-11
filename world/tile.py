import pygame as pg

from sprite.sprite import Sprite, Globals


class Tile(Sprite):

    def __init__(self, x, y, path):
        super().__init__(path_to_texture=path,
                         x=x,
                         y=y,
                         has_animation=False)
        self.x = x
        self.y = y
        self.width = Globals.tile_width
        self.height = Globals.tile_height
        self.pos = (self.x, self.y)

        self.rect = pg.rect.Rect(self.x, self.y, self.width, self.height)

        self.container = []

        self.is_traversable = True


    def draw(self, screen: pg.surface):
        screen.blit(self.texture, self.pos)
        for element in self.container:

            # repositioning the element to the tile's coordinates
            # so that it gets drawn at the right place, over the tile
            element.x = self.x
            element.rect.x = self.x
            element.y = self.y
            element.rect.y = self.y

            element.draw(screen)
