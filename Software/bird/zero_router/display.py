#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys

import pygame
import requests
from pygame.locals import *

print('sd',pygame.init())
# print(pygame.display.Info())
# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# set up the window
DISW, DISH = pygame.display.list_modes()[0]
print(DISH)

DISPLAYSURF = pygame.display.set_mode((DISW, DISH), FULLSCREEN, 32)
pygame.display.set_caption('Drawing')


# draw on the surface object
DISPLAYSURF.fill(WHITE, rect=None, special_flags=0)
pygame.draw.polygon(DISPLAYSURF, BLACK, ((DISW//10, DISH//10),
                                       (DISW//10, 9*DISH//10), (4*DISW//10, 9*DISH//10), (4*DISW//10, 1*DISH//10)))
pygame.draw.circle(DISPLAYSURF, GREEN, (7*DISW//10, DISH//2), DISH//5, 0)
fps = 15
fcclock = pygame.time.Clock()

def touch(pos):
    x, y = pos
    url = 'http://169.254.206.186:8080/bird'
    data ={'x':x}
    # data = {'time': time,  'pos_x': x, 'pos_y': y,'status':status,'action':action}
    try:
        req = requests.post(url, data)  # 发送post请求，第一个参数是URL，第二个参数是请求数据
        print(req)
    except Exception as e:
        print(e)

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
    fcclock.tick(fps)

# spamRect = pygame.Rect(10,20,200,300)

# TODO:
'''
1. 插入图片及其后续处理
2.
'''