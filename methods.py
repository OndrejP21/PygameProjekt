from base64 import decode
from tokenize import Number, String
import pygame as pg
import time
import json
from settings import *
import codecs

def StringToBool(stringBool):
    if (stringBool == "true"):
        return True
    else:
        return False

def ChangePlayerPosition(x, y):
    statsFileName = "story/stats.txt"
    statsFile = open(statsFileName, "r+")
    actualStats = json.loads(statsFile.read())

    actualStats["player_position"] = {"x": x, "y": y}
    statsFile.seek(0)
    statsFile.write(str(actualStats).replace("'", "\""))
    statsFile.truncate()
    statsFile.close()

transfer = 2.5373932

def WriteText(screen, fileName: String, line: Number):
    array = []

    pg.font.init()

    font = pg.font.Font("roboto.ttf", 20)

    offsetHeight = 380

    fontHeight = font.size("l")[0] * transfer * 2
    fontWidth = font.size("l")[1] / transfer

    dialogRectWidth = WIDTH
    dialogRectHeight = 400

    text =  font.render("", True, WHITE, BLACK)
    txt = (codecs.open(fileName, "r", "UTF-8").read().split(";")[2*line - 1])
    tx = ""

    i = 0
    actualRows = 0
    rows = 0

    timeBool = True

    while i < len(txt):
        pg.draw.rect(screen, BLACK, ((0, HEIGHT - dialogRectHeight), (dialogRectWidth, dialogRectHeight)))
        if txt[i] == " ":
            if i != len(txt):
                tx += txt[i]
                tx += txt[i + 1]       
                i += 1                        
        else:
            tx += txt[i]

        if ((i * fontWidth) - (WIDTH - 20) * rows) >= (dialogRectWidth - 80):
            if tx[len(tx) - 1] == " ":
                array.append(tx)
                tx = ""
                actualRows += 1
                rows += 1
            else:
                index = 0
                while tx[len(tx) + index - 1] != " ":
                    index -= 1
                i += index
                array.append(tx[0:len(tx) + index])
                tx = ""
                actualRows += 1
                rows += 1

            if (actualRows * fontHeight) >= dialogRectHeight - 100:

                continueRect = pg.Rect(WIDTH - 80, HEIGHT - 60, 60, 40)
                pg.draw.rect(screen, ORANGE, continueRect)
                continueText = font.render(">>>", True, BLACK, ORANGE)
                screen.blit(continueText, (WIDTH - 70, HEIGHT - 60))
                pg.display.flip()

                click = True
                while (click):
                    RenderArray(screen, font, array, offsetHeight, fontHeight)
                    pg.display.flip()
                    for event in pg.event.get():
                        if event.type == pg.MOUSEBUTTONDOWN and continueRect.collidepoint(pg.mouse.get_pos()):
                            actualRows = 0
                            array.clear()
                            click = False
                            timeBool = True

        i += 1

        RenderArray(screen, font, array, offsetHeight, fontHeight)

        text = font.render(tx, True, WHITE, BLACK)
        screen.blit(text, (20, HEIGHT - (offsetHeight - fontHeight * actualRows)))
        
        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                timeBool = not timeBool

        if timeBool:
            time.sleep(0.01)

       

def RenderArray(screen, font, array, offsetHeight, fontHeight):
    for j in range(len(array)):
        firstText = font.render(array[j], True, WHITE, BLACK)
        screen.blit(firstText, (20, HEIGHT - (offsetHeight - fontHeight * j)))