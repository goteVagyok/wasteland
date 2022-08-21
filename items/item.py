from sprite.sprite import Sprite


class Item(Sprite):

    def __init__(self, texture, x, y, has_animation, stack_size, item_id):
        super().__init__(texture, x, y, has_animation)
        self.stack_size = stack_size
        self.item_id = item_id

    def get(self):
        return self
