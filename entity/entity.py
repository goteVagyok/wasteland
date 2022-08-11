from sprite.sprite import Sprite
from utils.globals import Globals

Globals = Globals()


class Entity(Sprite):

    def __init__(self, path_to_texture, x, y, hp, has_animation):
        super().__init__(path_to_texture, x, y, has_animation)

        self.hp = hp
        self.can_move = True

        self.item_container = []
        self.item_container_capacity = 8

        self.tx = 0
        self.ty = 0

        self.max_tx = Globals.window_width / Globals.tile_width
        self.max_ty = Globals.window_height / Globals.tile_height
        # the entity will be in game_world.container[tx][ty]
        # tx and ty store the players indexes in the game_world container


    def add_to_container(self, item):
        if len(self.item_container) < self.item_container_capacity:
            self.item_container.append(item)
            Globals.debug(f"added {item.name}")
        else:
            Globals.debug(f"[ERR] container full")


    def move(self, event):
        pass
