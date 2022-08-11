import pygame as pg
from utils.globals import Globals


Globals = Globals()


class Sprite:


    def __init__(self, path_to_texture, x: int, y: int, has_animation: bool):
        """
        :param path_to_texture: path to the texture / keyframes of the sprite
        :param x: x coordinate of the sprite
        :param y: y coordinate of the sprite
        :param has_animation: whether the sprite has an animation (multiple keyframes)
        """

        self.path_to_texture = path_to_texture.value
        self.x = x
        self.y = y

        self.texture = pg.image.load(self.path_to_texture).convert_alpha()
        self.has_animation = has_animation

        self.rect = pg.rect.Rect(self.x, self.y, self.texture.get_width(), self.texture.get_height())

    def draw(self, screen):
        screen.blit(self.texture, self.rect)
