from enum import Enum
from utils.globals import Globals

G = Globals()
path = G.texture_path + "/textures/"


class Textures(Enum):
    PLAYER = path + "player/Player.png"
    TILE = path + "tiles/Tile.png"
    BLOCKADE = path + "tiles/Blockade.png"
    INVENTORY_SEGMENT = path + "player/inventory_segment.png"
