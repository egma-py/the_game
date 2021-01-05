from constants import *
from draw_functions import *
from colors import *
from figures import *
from menu import *

import pygame as pg
import pygame.draw as pgd
import pygmae.display as pgdis
import math as np

pg.init()
display_info = pgdis.Info()
display_size = (display_info.current_w, display_info.current_h)

screen = pgdis.set_mode(window_size)
clock = pg.time.Clock()

finished = False
fullscreen_mode = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        if event.type == pg.KEYDOWN and event.key == pg.K_F11:
            fullscreen_mode = not fullscreen_mode
            #FIXME recaculate objects' size and coords
            if fullscreen_mode:
                screen = pgdis.set_mode(display_size, fullscreen_flag)
            else:
                screen = pgdis.set_mode(window_size)
    screen.fill(DARK_YELLOW)
    pg.display.update()

pg.quit()