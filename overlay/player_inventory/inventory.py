from assets.texture_enum.textures import Textures
from overlay.overlay import OverlayComponent
from overlay.player_inventory.inventory_segment import InventorySegment
from utils.globals import Globals

Globals = Globals()


class Inventory(OverlayComponent):

    def __init__(self):
        super().__init__(100, 100, Textures.INVENTORY_SEGMENT)

        self.container: list[InventorySegment] = []
        self.slots = len(self.container)

        # TODO make inventory a collection of inv. segments (separate class). each segment should display its item
        #  and the number of them or smth. like that

    def add_item(self, item):
        for segment in self.container:
            if segment.has_item:
                if segment.container[0].item_id == item.item_id:
                    if item.stack_size > len(self.container):
                        segment.add_item(item)
            else:
                segment.add_item(item)

    def center_segments(self):
        offset = 0
        for seg in self.container:
            inv_bar_width = len(self.container) * seg.rect.w
            x = (Globals.window_width - inv_bar_width) / 2 + offset
            y = Globals.window_height - seg.rect.h
            offset += seg.rect.w

            seg.x = x
            seg.y = y
            seg.rect.x = x
            seg.rect.y = y

    def add_segment(self, number=1):
        for n in range(number):
            self.container.append(InventorySegment())
        self.center_segments()

    def draw(self, screen):
        for item in self.container:
            item.draw(screen)
