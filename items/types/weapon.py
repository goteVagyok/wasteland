from items.ids import Ids
from items.item import Item


class Weapon(Item):

    def __init__(self, texture, x: int, y: int, has_animation: bool, stack_size: int, reach_distance: int, damage: int):
        super().__init__(texture, x, y, has_animation, stack_size, Ids.weapon)

        self.reach_distance = reach_distance
        self.damage = damage
