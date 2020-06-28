#coding=utf-8
import time
import RPi.GPIO as GPIO
import logging
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
PINLIGHT = 16
PININPUT = 12


GPIO.setup(PINLIGHT, GPIO.OUT)
GPIO.setup(PININPUT,GPIO.IN)
# GPIO.setup(22, GPIO.OUT)
  
# p = GPIO.PWM(12,50)  # 通道为 12 频率为 50Hz
p=GPIO.PWM(PINLIGHT,5000)
# q=GPIO.PWM(22,5000)
p.start(0)
p.ChangeDutyCycle(100)
# # q.ChangeDutyCycle(1)
time.sleep(6)
# p.ChangeDutyCycle(90)
# p.stop()

# GPIO.cleanup()
# i=4

# try:
#     while i<=10:
#         print(i)
#         p.ChangeDutyCycle(i*10)
#         i=i+2
        
#         time.sleep(3)

# except KeyboardInterrupt:    
#     logging.info("ctrl + c:")
#     p.stop()

#     GPIO.cleanup()


p.stop()

GPIO.cleanup()        
