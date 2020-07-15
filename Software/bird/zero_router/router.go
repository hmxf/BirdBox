package main

import (
	"encoding/json"
	"fmt"
	"github.com/gin-gonic/gin"
	"io/ioutil"
	"os"
	"regexp"
	"syscall"
	"time"
)

var pid *os.Process

func main() {
	fmt.Println("hello world!")
	r := gin.Default()

	r.GET("/display", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "open the test",
		})
		if pid != nil {
			pid.Kill()
		}
		env := os.Environ()
		procAttr := &os.ProcAttr{
			Env: env,
			Files: []*os.File{
				os.Stdin,
				os.Stdout,
				os.Stderr,
			},
		}
		var err error
		//4b上测试
		//pid, err = os.StartProcess("/home/pi/BirdBox/Software/bird/zero_router/display.py", []string{""}, procAttr)
		//zero上测试
		pid, err = os.StartProcess("./base.py", []string{"3"}, procAttr)
		// pid, err = os.StartProcess("/home/pi/router/text/base.py", []string{"3"}, procAttr)
		if err != nil {
			fmt.Printf("Error %v starting process!", err) //
		}

	})
	r.GET("close", func(c *gin.Context) {
		fmt.Println(pid)
		if pid != nil {
			// pid.Release()
			pid.Signal(syscall.SIGINT)
		}
	})
	r.GET("print", func(c *gin.Context) {
		fmt.Println(pid)
	})
	r.GET("list", func(c *gin.Context) {
		files, _ := ioutil.ReadDir("./")
		var data []FileMessage
		for _, f := range files {
			fmt.Println(f.Name())
			if !isPy(f.Name()) {
				continue
			}
			var temp FileMessage
			var cstSh, _ = time.LoadLocation("Asia/Shanghai")
			temp.Name = f.Name()
			temp.Time = f.ModTime().In(cstSh).Format("2006-01-02 15:04:05")
			data = append(data, temp)
		}
		fmt.Println(data)
		jsons, _ := json.Marshal(data)#!/usr/bin/env python3
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
		c.JSON(200, jsons)
	})

	r.POST("script", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "open the test",
		})
		scriptName := c.PostForm("script_name")
		sleepTime := c.PostForm("sleep_time")
		if pid != nil {
			pid.Signal(syscall.SIGINT)
		}
		env := os.Environ()
		procAttr := &os.ProcAttr{
			Env: env,
			Files: []*os.File{
				os.Stdin,
				os.Stdout,
				os.Stderr,
			},
		}
		var err error
		//4b上测试
		//pid, err = os.StartProcess("/home/pi/BirdBox/Software/bird/zero_router/display.py", []string{""}, procAttr)
		//zero上测试
		pid, err = os.StartProcess("./"+scriptName, []string{sleepTime}, procAttr)
		// pid, err = os.StartProcess("/home/pi/router/text/base.py", []string{"3"}, procAttr)
		fmt.Printf("Error %v starting process!", err) //
		fmt.Println(pid)
	})
	// })
	r.Run() // 监听并在 0.0.0.0:8080 上启动服务
}

//FileMessage 文件信息
type FileMessage struct {
	Name string `json:"name"`
	Time string `json:"time"`
}

func isPy(str string) bool {

	reg, err := regexp.Compile(`.*\.py$`)
	if err != nil {
		fmt.Println(err)
		return false
	}
	return reg.MatchString(str)
}
