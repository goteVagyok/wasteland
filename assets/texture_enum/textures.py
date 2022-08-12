from enum import Enum
from utils.globals import Globals

G = Globals()
path = G.texture_path + "/textures/"


class Textures(Enum):
    # PLAYER
    PLAYER = path + "player/Player.png"
    # TILES
    TILE = path + "tiles/Tile.png"
    BLOCKADE = path + "tiles/Blockade.png"
    # UI
    INVENTORY_SEGMENT = path + "player/inventory_segment.png"
    INVENTORY_SEGMENT_HIGHLIGHTED = path + "player/inventory_segment_highlighted.png"
    # ITEMS
    LONGSWORD = path + "items/longsword.png"
