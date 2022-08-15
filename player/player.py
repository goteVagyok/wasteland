import pygame as pg

from assets.texture_enum.textures import Textures
from entity.entity import Entity
from overlay.player_inventory.inventory import Inventory
from settings.settings import Settings
from utils.globals import Globals

Globals = Globals()
Globals.DEBUG = False


class Player(Entity):

    def __init__(self, x, y, hp):
        super().__init__(Textures.PLAYER,
                         x,
                         y,
                         hp,
                         has_animation=True)

        self.inventory = Inventory()
        self.inventory.add_segment(5)
        self.inventory.container.reverse()
        self.inventory_shown = False

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

    def toggle_inventory_screen(self, event: pg.event):
        if event.type == pg.KEYDOWN:
            if event.key == Settings.key_toggle_inventory:
                self.inventory_shown = not self.inventory_shown
