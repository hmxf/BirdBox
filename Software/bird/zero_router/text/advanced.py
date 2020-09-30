#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys
import time

import pygame
import requests
from pygame.locals import *
import random

def sound():
    music = random.randint(1,2)
    global MUSIC 
    global MUSIC_UP
    MUSIC = music
    print(music)
    my_event = pygame.event.Event(MUSIC_UP, {"message": music})
    pygame.event.post(my_event)
    

def status_change(touchSpace):
    global STATUS
    global MUSIC
    statusCurrent = STATUS
    print("status_change:",touchSpace)
    url = 'http://169.254.206.186:8080/bird'
    data={
        'time':time.time(),
        'action':'Status Change'
    }
    if statusCurrent==0 and touchSpace == 2:
        pygame.draw.circle(DISPLAYSURF,RED,POS_IMG1 ,RADIUS)
        pygame.draw.circle(DISPLAYSURF,WHITE,POS_IMG2 ,RADIUS)
        pygame.draw.circle(DISPLAYSURF,RED,POS_IMG3 ,RADIUS)
        pygame.display.update()
        STATUS=1
        data={
            'time':time.time(),
            'action':'Status Change to Mode 1'
        }
        sound()
        postMessage(url,data)
        return
    if statusCurrent==1 and touchSpace == 1:
        music =  MUSIC
        if music == 1:#回答正确
            pygame.draw.circle(DISPLAYSURF,WHITE,POS_IMG1 ,RADIUS)
            pygame.draw.circle(DISPLAYSURF,WHITE,POS_IMG2 ,RADIUS)
            pygame.draw.circle(DISPLAYSURF,WHITE,POS_IMG3 ,RADIUS)
            pygame.display.update()
            reward()
            STATUS=0
            data={
                'time':time.time(),
                'action':'Status Change to Mode 0'
            }
            postMessage(url,data)
            return
    
    if statusCurrent==1 and touchSpace == 3:

        music =  MUSIC
        if music == 2:#回答正确
            pygame.draw.circle(DISPLAYSURF,WHITE,POS_IMG1 ,RADIUS)
            pygame.draw.circle(DISPLAYSURF,WHITE,POS_IMG2 ,RADIUS)
            pygame.draw.circle(DISPLAYSURF,WHITE,POS_IMG3 ,RADIUS)
            pygame.display.update()
            reward()       
            STATUS=0
            data={
                'time':time.time(),
                'action':'Status Change to Mode 0'
            }
            postMessage(url,data)
            return
    
    if touchSpace == 99:
        punish()
        pygame.draw.circle(DISPLAYSURF,WHITE,POS_IMG1 ,RADIUS)
        pygame.draw.circle(DISPLAYSURF,WHITE,POS_IMG2 ,RADIUS)
        pygame.draw.circle(DISPLAYSURF,WHITE,POS_IMG3 ,RADIUS)
        STATUS = 0
        data={
                'time':time.time(),
                'action':'Status Change to Mode 0'
            }
        postMessage(url,data)
        return

def reward():
    global MUSIC_DOWN
    url = http://169.254.206.186:8080/bird
    data={
            'time':time.time(),
            'x':x,
            'y':y,
            'action':'Give rewards'
        }
    postMessage(url,data)
    getRewards('http://169.254.206.186:8080/servo1')
    pygame.time.wait(3000)
    closeRewards('http://169.254.206.186:8080/servo2')
    my_event = pygame.event.Event(MUSIC_DOWN, {"message": "music down"})
    pygame.event.post(my_event)


# 奖励程序
def touch_base(pos):##
    x, y = pos
    url = 'http://169.254.206.186:8080/bird'
    data={
            'time':time.time(),
            'x':x,
            'y':y,
            'action':'Touch Screen'
        }
    if x > 62 and x < 262 and y > 200 and y < 400:
        status_change(1)
    if x > 412 and x < 612 and y > 200 and y < 400:
        status_change(2)
    if x > 762 and x < 962 and y > 200 and y < 400:
        status_change(3)
    postMessage(url,data)



def terminate():
    pygame.quit()
    sys.exit()

def twinkling(img_flag,state_flag,color):
    if state_flag==1:
        pos=POS_IMG1
    elif state_flag==2:
        pos=POS_IMG2
    elif state_flag==3:
        pos=POS_IMG3

    if img_flag%FPS==0 or img_flag%FPS==int(FPS/2):
        pygame.draw.circle(DISPLAYSURF,color,pos ,RADIUS)
        pygame.display.update()
    elif img_flag%FPS==int(FPS/4) or img_flag%FPS==int(3*FPS/4):
        # DISPLAYSURF.fill(WHITE,(POS_IMG,testingSize))
        pygame.draw.circle(DISPLAYSURF,WHITE,pos ,RADIUS)
        pygame.display.update()

def punish():
    global MUSIC_DOWN
    url='http://169.254.206.186:8080/bird'
    data={
            'time':time.time(),
            'x':x,
            'y':y,
            'action':'Music Down'
        }
    postMessage(url,data)
    my_event = pygame.event.Event(MUSIC_DOWN, {"message": "music down"})
    pygame.event.post(my_event)

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

    # goonSnd = pygame.mixer.Sound('src/goon.wav')
    biuSound = pygame.mixer.Sound("./src/biu.wav")
    biuSound.set_volume(0.2)
    funSound = pygame.mixer.Sound("./src/fun.wav")
    funSound.set_volume(0.2)



    fcclock = pygame.time.Clock()

    pygame.draw.circle(DISPLAYSURF,BLACK,POS_IMG1 ,RADIUS+3,3)
    pygame.draw.circle(DISPLAYSURF,BLACK,POS_IMG2 ,RADIUS+3,3)
    pygame.draw.circle(DISPLAYSURF,BLACK,POS_IMG3 ,RADIUS+3,3)
    pygame.display.update()
    img_flag =0
    music_flag =0
    global MUSIC
    while True:  # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
            elif event.type == MOUSEBUTTONUP:
                touch_base(event.pos)
            elif event.type == MUSIC_DOWN:
                print("down",MUSIC)
                if MUSIC == 1:
                    biuSound.stop()
                    MUSIC = 0
                else:
                    funSound.stop()
                    MUSIC = 0
            elif event.type == MUSIC_UP:
                print("up",MUSIC)
                music_flag = 1
                if MUSIC == 1:
                    biuSound.play()
                else:
                    funSound.play()


# 闪烁##
        if STATUS == 0:
            twinkling(img_flag,2,GREEN)
        elif STATUS ==1:
            if MUSIC ==1:
                twinkling(img_flag,1,RED)
            else:
                twinkling(img_flag,3,RED)
        img_flag = (img_flag+1)%FPS
        if music_flag != 0:
            music_flag+=1
        if music_flag == FPS*REACTIONTIME:
            music_flag =0
            status_change(99)
        fcclock.tick(FPS)


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DISPLAYSURF = pygame.display.set_mode((1024, 600)) 
RADIUS = 100
POS_IMG1 = (162,300)
POS_IMG2 = (512,300)
POS_IMG3 = (862,300)
FPS = 15
STATUS=0
MUSIC = 0
# 超时时间
REACTIONTIME = 15
# define event 
# music down
MUSIC_UP = pygame.USEREVENT + 1
#music up
MUSIC_DOWN = pygame.USEREVENT + 2
# draw on the surface object
DISPLAYSURF.fill(WHITE, rect=None, special_flags=0)

if __name__ == '__main__':
    main()
