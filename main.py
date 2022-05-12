import pygame as pg
import sys
from os import path

from pygame import sprite
from settings import *
import settings as settings
from sprites import *
from tilemap import *
from menu import *
import menu
from methods import *

statsFileName = "story/stats.txt"

class Game:
    def __init__(self):
        settings.rotx = 500 * (WIDTH / 1024)
        settings.roty = 360 * (HEIGHT / 768)
        settings.rotx1 = 500 * (WIDTH / 1024)
        settings.roty1 = 360 * (HEIGHT / 768)
        
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        graphics_folder = path.join(game_folder, 'graphics')
        map_folder = path.join(game_folder, "maps")
        self.map = TiledMap(path.join(map_folder, 'mapa.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(path.join(graphics_folder, PLAYER_IMG)).convert_alpha()
        self.mob_img = pg.image.load(path.join(graphics_folder, MOB_IMG)).convert_alpha()

    def new(self, player_position_x, player_position_y):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        #for row, tiles in enumerate(self.map.data):
            #for col, tile in enumerate(tiles):
                #if tile == 'P':
                    #self.player = Player(self, col, row)
                #if tile == '1':
                    #Wall(self, col, row)
                #if tile == '2':
                    #Mob(self, col, row)

        self.player = Player(self, player_position_x / TILESIZE, player_position_y / TILESIZE)
        self.camera = Camera(self.map.width, self.map.height, 0, 0)


    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
            pg.display.flip()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

        settings.rotx1 = settings.rotx
        settings.roty1 = settings.roty

        leftXProblem = WIDTH / 2
        upYProblem = HEIGHT / 2
        rightXProblem = self.map.width - leftXProblem
        downYProblem = self.map.height - upYProblem
            
        if (self.player.pos.x <= leftXProblem):
            settings.rotx1 = settings.rotx - self.camera.xx
        if (self.player.pos.y <= upYProblem):
            settings.roty1 = settings.roty - self.camera.yy
        if (self.player.pos.x >= rightXProblem):
            settings.rotx1 = settings.rotx + (self.player.pos.x - rightXProblem)
        if (self.player.pos.y >= downYProblem):
            settings.roty1 = settings.roty + (self.player.pos.y - downYProblem)
            
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, DARKGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, DARKGREY, (0, y), (WIDTH, y))

    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        #self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    ChangePlayerPosition(self.player.pos.x, self.player.pos.y)
                    m = menu.Menu()
                if event.key == pg.K_KP_ENTER:
                    print(self.camera.x)
            if event.type == pg.MOUSEMOTION:
                self.rotate()

    def rotate(self):
        pos = pg.mouse.get_pos()

        angle = 360 - math.atan2(pos[1] - settings.roty1, pos[0] - settings.rotx1) * 180 / math.pi
        
        self.player.image = pg.transform.rotate(self.player_img, angle)
        self.rect = self.player.image.get_rect(center = self.player.rect.center)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass