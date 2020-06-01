
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import sys

from pygame.locals import *
import requests
import json

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((500, 300), 0, 32)
pygame.display.set_caption('Drawing')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# draw on the surface object
DISPLAYSURF.fill(WHITE, rect=None, special_flags=0)
pygame.draw.polygon(DISPLAYSURF, RED, ((60, 60),
                                       (60, 240), (180, 240), (180, 60)))
pygame.draw.circle(DISPLAYSURF, GREEN, (350, 150), 90, 0)


def touch(x, y):
    url = 'http://localhost:8080/post_test'
    data = {'username': 'mpp0130', 'pwd': 'Mp123456',
            'cpwd': 'Mp123456', 'x': x, 'y': y}
    req = requests.post(url, data)  # 发送post请求，第一个参数是URL，第二个参数是请求数据


while True:  # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            touch(mousex, mousey)
    pygame.display.update()

# spamRect = pygame.Rect(10,20,200,300)

