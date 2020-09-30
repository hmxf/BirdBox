#coding=utf-8
import multiprocessing as mp
import time
import RPi.GPIO as GPIO

def gpio_init():  #初始化GPIO，设置初始角和信号输出口36
    
    global pwm
    global num_
    global angle
    angle = 90
    num_ = 0
    GPIO.setmode(GPIO.BOARD)
    # GPIO.setup(40,GPIO.IN)
    GPIO.setup(38, GPIO.OUT)
    pwm = GPIO.PWM(38, 50)
    pwm.start(10 / 180 * 90 + 2)
    pwm.ChangeDutyCycle(0)  #清空占空比，这句是防抖关键句，如果没有这句，舵机会狂抖不止

def show_cap(): #死循环
    while(1):
        if GPIO.input(40):
            break
            
def setDirection(direction):  
    duty = 10 / 180 * direction + 2
    pwm.ChangeDutyCycle(duty)
    print("direction =", direction, "-> duty =", duty)   
    time.sleep(0.04) #等待控制周期结束
    pwm.ChangeDutyCycle(0)   #清空占空比，这句是防抖关键句，如果没有这句，舵机会狂抖不止
    
def runrun():

    gpio_init()
    show_cap()
    GPIO.cleanup()
    
if __name__=='__main__':

    runrun()
