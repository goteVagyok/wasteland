from world.tile import Tile
from utils.globals import Globals
from assets.texture_enum.textures import Textures

Globals = Globals()


class Blockade(Tile):

    def __init__(self, x, y):
        super().__init__(x, y, Textures.BLOCKADE)
        self.is_traversable = False
