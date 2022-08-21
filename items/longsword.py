from assets.texture_enum.textures import Textures
from items.ids import Ids
from items.types.weapon import Weapon


class LongSword(Weapon):

    def __init__(self, x, y, has_animation=False, stack_size=12):
        super().__init__(Textures.LONGSWORD, x, y, has_animation, stack_size, 5, 6)
        self.item_id += Ids.LONGSWORD
