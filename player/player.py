import pygame as pg

from assets.texture_enum.textures import Textures
from entity.entity import Entity
from settings.settings import Settings
from sprite.sprite import Sprite
from utils.globals import Globals


Globals = Globals()


class Player(Entity):

    def __init__(self, x, y, hp):
        super().__init__(Textures.PLAYER,
                         x,
                         y,
                         hp,
                         has_animation=True)

        self.segment = Sprite(Textures.INVENTORY_SEGMENT, 100, 100, False)


    def move(self, event: pg.event) -> tuple[int, int]:
        """

        :param event: pygame event
        :return: the target x and y of the player.
                 no movement is done in here
        """
        # TODO make a crude movement ai in entity

        target_x = self.tx
        target_y = self.ty

        if event.type == pg.KEYDOWN:

            if event.key == Settings.key_up:  # up
                Globals.debug(f"keypress: w")
                if target_y - 1 >= 0:
                    target_y -= 1

            elif event.key == Settings.key_left:  # left
                Globals.debug(f"keypress: a")
                if target_x - 1 >= 0:
                    target_x -= 1

            elif event.key == Settings.key_down:  # down
                Globals.debug(f"keypress: s")
                if target_y + 1 < self.max_ty:
                    target_y += 1

            elif event.key == Settings.key_right:  # right
                Globals.debug(f"keypress: d")
                if target_x + 1 < self.max_tx:
                    target_x += 1

        return target_x, target_y


    def toggle_inventory_screen(self, event: pg.event, screen):
        shown = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_e:
                shown = not shown
                print(shown)

        if shown:
            Globals.debug("inventory shown.")
            self.segment.draw(screen)  # TODO needs to be drawn above game_world to be visible
