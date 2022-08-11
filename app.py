# wasteland main project file

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "True"

import pygame as pg

from player.player import Player
from utils.globals import Globals
from window.window import Window
from world.world import GameWorld

Globals = Globals()

Globals.debug("run script.")

WINDOW = Window(Globals.window_width, Globals.window_height)
RUN = True
game_world = GameWorld()

player = Player(0, 0, 100)

game_world.container[player.tx][player.ty].container.append(player)


pg.key.set_repeat(200, 100)

# prev_time = time()

# testing ssh auth form manjaro machine

while RUN:

    WINDOW.update()

    # now = time()
    # Globals.dt = now - prev_time
    # prev_time = now

    for event in pg.event.get():
        if event.type == pg.QUIT:
            RUN = False

        prev_tx = player.tx
        prev_ty = player.ty

        game_world.move_entity(player, (prev_tx, prev_ty), event)
        # player.toggle_inventory_screen(event, WINDOW.screen)

        game_world.update(WINDOW.screen)
