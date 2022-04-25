from cmath import rect
import pygame as pg
import ctypes as ct
from screeninfo import get_monitors
from os import path

def init():
    global rotx
    global roty
    global rotx1
    global roty1
    global maxx
    global maxy
    global maxx1
    global maxy1

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
DARK = (192, 192, 192)
ORANGE = (168, 80, 50)

WIDTH = get_monitors()[0].width  # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = get_monitors()[0].height # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = DARKGREY
CAT = pg.image.load(path.join('img/cat.png'))
BACKGROUND = "img/background.png"

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

PLAYER_SPEED = 300
MOB_SPEED = 150
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'PNG/Hitman1/hitman1_gun.png'
#MOB_IMG = 'PNG/Zombie1/zoimbie1_gun.png'
MOB_IMG = 'pica.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
MOB_HIT_RECT = pg.Rect(0,0,30,30)