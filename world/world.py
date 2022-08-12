from utils.globals import Globals
from assets.texture_enum.textures import Textures

from world.tile import Tile
from world.blockade import Blockade

Globals = Globals()


class GameWorld:

    def __init__(self):
        self.tile_container: list[list[Tile | Blockade]] = []  # container for all world elements (eg.: Tiles, etc)
        self.UI_container = []  # container for all ui elements such as inventory and esc menu overlay

        for x in range(0, Globals.window_width, Globals.tile_width):
            row = []
            for y in range(0, Globals.window_height, Globals.tile_height):
                if x == 50 and y == 50:
                    row.append(Blockade(x, y))
                else:
                    row.append(Tile(x, y, Textures.TILE))
            self.tile_container.append(row)

    def move_entity(self, entity, prev_coordinates, event):
        if entity.can_move:

            target_x, target_y = entity.move(event)
            target_tile = self.tile_container[target_x][target_y]

            if target_tile.is_traversable:

                prev_tile = self.tile_container[prev_coordinates[0]][prev_coordinates[1]]
                target_tile.container.append(entity)

                entity.tx = target_x
                entity.ty = target_y

                prev_tile.container.pop(0)

            else:
                Globals.debug("target is not traversable")

    def handle_player_ui_elements(self, player, event):
        player.toggle_inventory_screen(event)

        if player.inventory_shown:

            if player.inventory not in self.UI_container:
                self.UI_container.append(player.inventory)
                Globals.debug("player inv. added to UI_container")

        else:
            if player.inventory in self.UI_container:
                self.UI_container.pop(self.UI_container.index(player.inventory))
                Globals.debug("player inv. removed form UI_container")

    def update(self, screen):
        for row in self.tile_container:
            for e in row:
                e.draw(screen)

        for element in self.UI_container:
            element.draw(screen)
