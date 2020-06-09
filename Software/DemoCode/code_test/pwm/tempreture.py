#coding=utf-8
import time
import RPi.GPIO as GPIO
import logging
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
PINLIGHT = 36


GPIO.setup(PINLIGHT, GPIO.OUT)

  
# p = GPIO.PWM(12,50)  # 通道为 12 频率为 50Hz
p=GPIO.PWM(PINLIGHT,1000)

p.start(0)

try:
    while True:
        p.ChangeDutyCycle(50)

except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    p.stop()

    GPIO.cleanup()
    exit()

        
p.stop()

GPIO.cleanup()
