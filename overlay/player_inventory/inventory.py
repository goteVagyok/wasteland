from assets.texture_enum.textures import Textures
from overlay.overlay import OverlayComponent
from overlay.player_inventory.inventory_segment import InventorySegment
from utils.globals import Globals, Colors

Globals = Globals()


class Inventory(OverlayComponent):

    def __init__(self):
        super().__init__(100, 100, Textures.INVENTORY_SEGMENT)

        self.container: list[InventorySegment] = []
        self.slots = len(self.container)

    def add_item(self, item):
        for segment in self.container:
            if segment.has_item:
                if segment.container[0].item_id == item.item_id:
                    if item.stack_size > len(segment.container):
                        segment.add_item(item)
                        segment.has_item = True
                        self.position_number_of_items(segment)
                        break
            else:
                segment.add_item(item)
                segment.has_item = True
                self.position_number_of_items(segment)
                break

    @staticmethod
    def position_number_of_items(segment: InventorySegment):
        n_of_item = Globals.mono_font.render(str(segment.num_of_items), 0, Colors.black)
        offset = 7  # offset of the segment outline
        text_rect = n_of_item.get_rect()
        x = segment.x + (segment.rect.w - offset - text_rect.w)
        y = segment.y + (segment.rect.h - offset - text_rect.h)

        segment.num_of_items_font = n_of_item
        segment.num_of_items_pos = (x, y)

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

            self.position_number_of_items(seg)

    def add_segment(self, number=1):
        for n in range(number):
            self.container.append(InventorySegment())
        self.center_segments()

    def draw(self, screen):
        for item in self.container:
            item.draw(screen)
