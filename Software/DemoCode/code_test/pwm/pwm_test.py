#coding=utf-8
import time
import RPi.GPIO as GPIO
import logging
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
PINLIGHT = 16


GPIO.setup(PINLIGHT, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
  
# p = GPIO.PWM(12,50)  # 通道为 12 频率为 50Hz
p=GPIO.PWM(PINLIGHT,1000)
q=GPIO.PWM(22,1000)
p.start(0)
q.start(0)
try:
    while True:
        p.ChangeDutyCycle(5)
        q.ChangeDutyCycle(5)
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    p.stop()
    q.stop()
    GPIO.cleanup()
    exit()

        
p.stop()
q.stop()
GPIO.cleanup()

