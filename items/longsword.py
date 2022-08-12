from assets.texture_enum.textures import Textures
from items.item import Item


class LongSword(Item):

    def __init__(self, x, y, has_animation=False, stack_size=1):
        super().__init__(Textures.LONGSWORD, x, y, has_animation, stack_size)
