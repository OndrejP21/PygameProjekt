#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
from array import array
from asyncio.windows_events import NULL
from turtle import screensize
import pygame, sys
 
# Setup Python ----------------------------------------------- #
import main as m
import json
from main import *
from pygame.locals import *
from settings import *
from methods import *
# Setup pygame/window ---------------------------------------- #

statsFile = open("story/stats.txt", "r+")

class Menu:

    def __init__(self):       
        mainClock = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption('game base')
        screen = pygame.display.set_mode((1920,1080))
        background = pygame.image.load(BACKGROUND)
        background = pygame.transform.scale(background,(1920, 1080))
        white = (255, 255, 255)
        green = (0, 255, 0)
        blue = (0, 0, 128)
        pygame.font.init()
        myfont = pygame.font.SysFont('calibri', 30)

        #start = json.loads(star)

        font = pygame.font.SysFont(None, 20)

        def draw_text(text, font, color, surface, x, y):
            textobj = font.render(text, 1, color)
            textrect = textobj.get_rect()
            textrect.topleft = (x, y)
            surface.blit(textobj, textrect)

        click = False

        def menu():
            running = True
            while running:
                screen.fill((0,0,0))
                textsurface = myfont.render('Some Text', False, (69,69,69))
                button_MenuGAME = pygame.Rect(350, 500, 250, 50)
                button_MENU = pygame.Rect(350, 600, 250, 50)
                pygame.draw.rect(screen, (255, 255, 255), button_MenuGAME)
                pygame.draw.rect(screen, (255, 255, 255), button_MENU)
                screen.blit(textsurface,(370,500))
                
                draw_text('characters', font, (255, 255, 255), screen, 20, 20)
                for event in pygame.event.get():
                    pygame.display.update()
                    mainClock.tick(60)
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            running = False
                
                
        def characters():
            running = True
            while running:
                screen.fill((0,0,0))
                
                draw_text('characters', font, (255, 255, 255), screen, 20, 20)
                for event in pygame.event.get():
                    pygame.display.update()
                    mainClock.tick(60)
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            running = False
                            

        def inventory():
            running = True
            while running:
                screen.fill((0,0,0))
                
                draw_text('inventory', font, (255, 255, 255), screen, 20, 20)
                pygame.display.update()
                mainClock.tick(60)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            running = False


        def options():
            running = True
            while running:
                screen.fill((0,0,0))

                draw_text('options', font, (255, 255, 255), screen, 20, 20)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            running = False
                
                pygame.display.update()
                mainClock.tick(60)

        def LoadGame():
            running = True
            while running:
                screen.fill((0,0,0))

                draw_text('loadGame', font, (255, 255, 255), screen, 20, 20)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            running = False
                
                pygame.display.update()
                mainClock.tick(60)

        def StartGame():
            g = m.Game()
            while True:
                g.new()
                g.run()
            
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            running = False
                
                pygame.display.update()
                mainClock.tick(60)

        def NewGame():
            actualStats = json.loads(statsFile.read())

            if (not StringToBool(actualStats["start"])):
                pg.init()
                
                while True:
                    screen = pg.display.set_mode((WIDTH, HEIGHT))
                    screen.fill((102, 100, 93))

                    WriteText(screen, "story/start/text.txt", 0)
                    actualStats["start"] = str(True).lower()
                    statsFile.seek(0)
                    statsFile.write(str(actualStats).replace("'", "\""))
                    statsFile.truncate()
                    statsFile.close()
                    break
                StartGame()
            else:
                StartGame()

        def quit():
            pygame.quit()
            sys.exit()


        while True:
            click = False
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            mainClock.tick(60)

            screen.fill((0,0,0))
            draw_text('main menu', font, (255, 255, 255), screen, 20, 20)

            mx, my = pygame.mouse.get_pos()

            button_1 = pygame.Rect(350, 415, 250, 50)
            button_2 = pygame.Rect(350, 500, 250, 50)
            button_3 = pygame.Rect(350, 590, 250, 50)
            button_4 = pygame.Rect(350, 695, 250, 50)
            

            if button_1.collidepoint((mx, my)):
                if click:
                    NewGame()
            if button_2.collidepoint((mx, my)):
                if click:
                    NewGame()
            if button_3.collidepoint((mx, my)):
                if click:
                    NewGame()
            if button_4.collidepoint((mx, my)):
                if click:
                    quit()

            screen.blit(background,(0,0)) 
            
            pygame.display.update()
            pygame.display.flip()

m = Menu()
m