import pygame as pg
import pygame.draw as pgd
import math as np

from constants import *
from draw_functions import *
from colors import *

pg.init()
screen = pg.display.set_mode(window_size)
clock = pg.time.Clock()

finished = False
phase = 0
angle0 = 40 + int(20*m.sin(phase))

while not finished:
    phase += 0.1
    angle0 = 40 + int(20*m.sin(phase))
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
    screen.fill(DARK_YELLOW)
    pie(screen, RED, ((200, 200), (300, 200)), angle0, 360)
    pg.display.update()

pg.quit()