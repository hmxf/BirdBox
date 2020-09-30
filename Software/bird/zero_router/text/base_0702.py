#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys
import time

import pygame
import requests
from pygame.locals import *


def touch(pos,rewardTime):
    x, y = pos
    url=URL
    data={
            'time':time.time(),
            'x':x,
            'y':y,
            'action':'Touch Screen'
        }

    if x > 412 and x < 612 and y > 200 and y < 400:
        dianzanGreenImg = pygame.image.load("src/green_icon/dianzan.png")
        DISPLAYSURF.blit(dianzanGreenImg, (412, 200))
        pygame.display.update()
        data={
            'time':time.time(),
            'x':x,
            'y':y,
            'action':'Touch the Start-Button',
        }

        postMessage(url,data)
        getRewards('http://192.168.0.6:8081/servo2')
        time.sleep(rewardTime)
        dianzanImg = pygame.image.load("src/black_icon/dianzan.png")
        DISPLAYSURF.blit(dianzanImg, (412, 200))
        pygame.display.update()
        data={
            'time':time.time(),
            'x':x,
            'y':y,
            'action':'Reward time up!',
        }
        postMessage(url,data)
        closeRewards('http://192.168.0.6:8081/servo1')
        pygame.event.clear()
    else:
        postMessage(url,data)


def terminate():
    data={
            'time':time.time(),
            'action':'Quit the test',
        }
    postMessage(URL,data)
    pygame.quit()
    sys.exit()


def postMessage(url,data):
    try:
        req = requests.post(url, data)  # 发送post请求，第一个参数是URL，第二个参数是请求数据
        print(req)
    except Exception as e:
        print(e)

def getRewards(url):
    try:
        req=requests.get(url)
    except Exception as e:
        print(e)

def closeRewards(url):
    try:
        req=requests.get(url)
    except Exception as e:
        print(e)

def main():

    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption('Drawing')
    rewardTime = 5
    if len(sys.argv) != 1:
        rewardTime = int(sys.argv[1])
    # print(type(rewardTime))
    print(int(rewardTime))
    data={
            'time':time.time(),
            'action':'Start the test: '+sys.argv[0],
        }
    postMessage(URL,data)
    dianzanImg = pygame.image.load("src/black_icon/dianzan.png")

    goonSnd = pygame.mixer.Sound('src/goon.wav')

    fps = 15
    fcclock = pygame.time.Clock()

    DISPLAYSURF.blit(dianzanImg, (412, 200))
    pygame.display.update()
    while True:  # main game loop

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
            elif event.type == MOUSEBUTTONUP:
                touch(event.pos,rewardTime)

        fcclock.tick(fps)





BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DISPLAYSURF = pygame.display.set_mode((1024, 600),FULLSCREEN)
# URL = 'http://169.254.206.186:8080/bird'
URL ='http://192.168.0.6:8080/bird'

# draw on the surface object
DISPLAYSURF.fill(WHITE, rect=None, special_flags=0)

if __name__ == '__main__':
    main()