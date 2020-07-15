#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys
import time

import pygame
import requests
from pygame.locals import *


# def touch(pos):
#     x, y = pos
#     url = 'http://169.254.206.186:8080/bird'
#     data={
#             'time':time.time(),
#             'x':x,
#             'y':y,
#             'action':'Touch Screen'
#         }
#     if x > 312 and x < 712 and y > 100 and y < 500:
#         testingGreenImg = pygame.image.load("src/green_icon/testing.png")
#         DISPLAYSURF.blit(testingGreenImg, POS_IMG)
#         pygame.display.update()
#         pygame.time.wait(1000)
#         testingImg = pygame.image.load("src/black_icon/testing.png")
#         DISPLAYSURF.blit(testingImg, POS_IMG)
#         pygame.display.update()

#     # data = {'time': time,  'pos_x': x, 'pos_y': y,'status':status,'action':action}
#     postMessage(url,data)

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


# 奖励程序
def reward(pos):##
    x, y = pos
    url = 'http://169.254.206.186:8080/bird'
    data={
            'time':time.time(),
            'x':x,
            'y':y,
            'action':'Touch Screen'
        }
    if x > 312 and x < 712 and y > 100 and y < 500:
        data={
            'time':time.time(),
            'x':x,
            'y':y,
            'action':'Touch The Button'
        }
        postMessage(url,data)
        pygame.draw.circle(DISPLAYSURF,WHITE,POS_IMG ,150)
        pygame.draw.circle(DISPLAYSURF,BLACK,POS_IMG ,150,3)
        pygame.display.update()
        getRewards('http://192.168.0.6:8081/servo2')
        pygame.time.wait(1000*RewardTime)
        print(RewardTime)
        closeRewards('http://192.168.0.6:8081/servo1')
    # data = {'time': time,  'pos_x': x, 'pos_y': y,'status':status,'action':action}
    else:
        postMessage(url,data)



def terminate():
    pygame.quit()
    sys.exit()


def main():
    global RewardTime
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption('Drawing')
    if len(sys.argv) != 1:
        RewardTime = int(sys.argv[1])
    print(RewardTime)
    fps = 15
    fcclock = pygame.time.Clock()

    pygame.display.update()
    img_flag =0
    while True:  # main game loop

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
            elif event.type == MOUSEBUTTONUP:
                reward(event.pos)

# 闪烁##
        if img_flag%fps==0 or img_flag%fps==int(fps/2):
            pygame.draw.circle(DISPLAYSURF,GREEN,POS_IMG ,150)
            pygame.display.update()
        elif img_flag%fps==int(fps/4) or img_flag%fps==int(3*fps/4):
            # DISPLAYSURF.fill(WHITE,(POS_IMG,testingSize))
            pygame.draw.circle(DISPLAYSURF,WHITE,POS_IMG ,150)
            pygame.draw.circle(DISPLAYSURF,BLACK,POS_IMG ,150,3)
            pygame.display.update()

        img_flag= (img_flag+1)%fps
        # print(img_flag)
        fcclock.tick(fps)


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DISPLAYSURF = pygame.display.set_mode((1024, 600)) 
POS_IMG = (512,300)
RewardTime = 3

# draw on the surface object
DISPLAYSURF.fill(WHITE, rect=None, special_flags=0)

if __name__ == '__main__':
    main()
