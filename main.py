import pygame as pg
import pygame.draw as pgd
import math as np

from constants import *
from draw_functions import *
from colors import *
from figures import *

pg.init()
display_info = pg.display.Info()
full_size = (display_info.current_w, display_info.current_h)

screen = pg.display.set_mode(window_size)
clock = pg.time.Clock()

finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
    screen.fill(DARK_YELLOW)
    
    pg.display.update()

pg.quit()