from assets.texture_enum.textures import Textures
from overlay.overlay import OverlayComponent
from overlay.player_inventory.inventory_segment import InventorySegment


class Inventory(OverlayComponent):

    def __init__(self):
        super().__init__(100, 100, Textures.INVENTORY_SEGMENT)

        self.container: list[InventorySegment] = []
        self.slots = len(self.container)

        # TODO make inventory a collection of inv. segments (separate class). each segment should display its item
        #  and the number of them or smth. like that

    def add_item(self, item):
        seg = InventorySegment()

        seg.add_item(item)
        self.container.append(seg)

    def draw(self, screen):
        for item in self.container:
            item.draw(screen)
