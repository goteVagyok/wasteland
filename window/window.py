import pygame as pg


class Window:

    def __init__(self, width, height, caption="wasteland"):
        self.width = width
        self.height = height
        self.size = (self.width, self.height)

        self.screen = pg.display.set_mode(self.size, pg.RESIZABLE)
        pg.display.set_caption(caption)

        # TODO make resized window be filled with tiles / scaled


    @staticmethod
    def update() -> None:
        pg.display.flip()

