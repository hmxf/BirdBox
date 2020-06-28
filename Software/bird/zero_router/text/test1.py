# -*- coding: utf-8 -*-

import json
import sys
import time

import pygame
import requests
from pygame.locals import *


def touch(pos,sound):
    x, y = pos
    url = 'http://169.254.206.186:8080/bird'
    if x > 312 and x < 712 and y > 100 and y < 500:
        sound.play()
        dianzanGreenImg = pygame.image.load("src/green_icon/dianzan.png")
        DISPLAYSURF.blit(dianzanGreenImg, (312, 100))
        time.sleep(3)
        # DISPLAYSURF.blit(anquanImg, (70, 100))
        # DISPLAYSURF.blit(caidanImg, (554, 100))
        sound.stop()

    data = {'x': x}
    # data = {'time': time,  'pos_x': x, 'pos_y': y,'status':status,'action':action}
    try:
        req = requests.post(url, data)  # 发送post请求，第一个参数是URL，第二个参数是请求数据
        print(req)
    except Exception as e:
        print(e)


def terminate():
    pygame.quit()
    sys.exit()


def main():

    pygame.init()
    pygame.mixer.init()

    # print(pygame.display.Info())
    # set up the colors


    # set up the window
    # DISW, DISH = pygame.display.list_modes()[0]
    # print(DISH)

    # DISPLAYSURF = pygame.display.set_mode((DISW, DISH), FULLSCREEN)

    # pygame.draw.polygon(DISPLAYSURF, BLACK, ((DISW//10, DISH//10),
    #                                        (DISW//10, 9*DISH//10), (4*DISW//10, 9*DISH//10), (4*DISW//10, 1*DISH//10)))
    # pygame.draw.circle(DISPLAYSURF, GREEN, (7*DISW//10, DISH//2), DISH//5, 0)
    # anquanImg = pygame.image.load("src/anquan.png")
    # caidanImg = pygame.image.load("src/caidan.png")
    dianzanImg = pygame.image.load("src/black_icon/dianzan.png")

    goonSnd = pygame.mixer.Sound('src/goon.wav')
    # goonSnd=pygame.mixer.music.load('src/goon.wma')
    fps = 120
    fcclock = pygame.time.Clock()

    DISPLAYSURF.blit(dianzanImg, (312, 100))
    while True:  # main game loop

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
            elif event.type == MOUSEBUTTONUP:
                touch(event.pos,goonSnd)
        pygame.display.update()
        fcclock.tick(fps)

    # spamRect = pygame.Rect(10,20,200,300)

    # TODO:
    '''
    1. 插入图片及其后续处理
    2. 
    '''

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DISPLAYSURF = pygame.display.set_mode((1024, 600))
pygame.display.set_caption('Drawing')

# draw on the surface object
DISPLAYSURF.fill(WHITE, rect=None, special_flags=0)

if __name__ == '__main__':
    main()
