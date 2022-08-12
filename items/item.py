from sprite.sprite import Sprite


class Item(Sprite):

    def __init__(self, texture, x, y, has_animation, stack_size):
        super().__init__(texture, x, y, has_animation)
        self.stack_size = stack_size
