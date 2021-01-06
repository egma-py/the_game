from constants import *
from draw_functions import *
from colors import *
from figures import *
from menu import *

import pygame as pg
import pygame.draw as pgd
import pygame.display as pgdis
import math as np

pg.init()
display_info = pgdis.Info()
display_size = (display_info.current_w, display_info.current_h)

screen = pgdis.set_mode(window_size)
clock = pg.time.Clock()

finished = False
fullscreen_mode = False

surf = pg.Surface((100, 100))
surf = surf.convert_alpha()
surf.fill((0, 255, 0, 255))
pol = Polygon(screen, RED, [[100, 100], [150, 100], [150, 150]], 4)
while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        if event.type == pg.KEYDOWN and event.key == pg.K_F11:
            fullscreen_mode = not fullscreen_mode
            #FIXME recaculate objects' size and coords depending on fullscreen mode
            if fullscreen_mode:
                screen = pgdis.set_mode(display_size, fullscreen_flag)
            else:
                screen = pgdis.set_mode(window_size)
    screen.fill(DARK_YELLOW)
    #pol.draw()
    roundrect(screen, RED, ((100, 100), (300, 200)), 0, 50, [50, 60, 0, 80])
    pgdis.update()

pg.quit()