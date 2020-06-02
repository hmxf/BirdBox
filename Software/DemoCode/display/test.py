
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import sys

from pygame.locals import *
import requests
import json

pygame.init()

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# set up the window
DISW,DISH=pygame.display.list_modes()[0]

DISPLAYSURF = pygame.display.set_mode((DISW,DISH), FULLSCREEN, 32)
pygame.display.set_caption('Drawing')





# draw on the surface object
DISPLAYSURF.fill(WHITE, rect=None, special_flags=0)
pygame.draw.polygon(DISPLAYSURF, RED, ((DISW//10, DISH//10),
                                       (DISW//10, 9*DISH//10), (4*DISW//10, 9*DISH//10), (4*DISW//10, 1*DISH//10)))
pygame.draw.circle(DISPLAYSURF, GREEN, (7*DISW//10, DISH//2), DISH//5, 0)


def touch(pos):
    x, y = pos
    url = 'http://localhost:8080/post_test'
    data = {'username': 'mpp0130', 'pwd': 'Mp123456',
            'cpwd': 'Mp123456', 'x': x, 'y': y}
    req = requests.post(url, data)  # 发送post请求，第一个参数是URL，第二个参数是请求数据

def terminate():
    pygame.quit()
    sys.exit()

while True:  # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                terminate()
        elif event.type == MOUSEBUTTONUP:
            touch(event.pos)
    pygame.display.update()

# spamRect = pygame.Rect(10,20,200,300)

