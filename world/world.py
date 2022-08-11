from utils.globals import Globals
from assets.texture_enum.textures import Textures
from world.tile import Tile

from world.blockade import Blockade


Globals = Globals()


class GameWorld:

    def __init__(self):
        self.container = []

        for x in range(0, Globals.window_width, Globals.tile_width):
            row = []
            for y in range(0, Globals.window_height, Globals.tile_height):
                if x == 50 and y == 50:
                    row.append(Blockade(x, y))
                else:
                    row.append(Tile(x, y, Textures.TILE))
            self.container.append(row)



    def move_entity(self, entity, prev_coordinates, event):
        if entity.can_move:

            target_x, target_y = entity.move(event)
            target_tile = self.container[target_x][target_y]

            if target_tile.is_traversable:

                prev_tile = self.container[prev_coordinates[0]][prev_coordinates[1]]
                target_tile.container.append(entity)

                entity.tx = target_x
                entity.ty = target_y

                prev_tile.container.pop(0)

            else:
                Globals.debug("target is not traversable")


    def update(self, screen):
        for row in self.container:
            for e in row:
                e.draw(screen)
