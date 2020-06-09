#coding=utf-8
import time
import RPi.GPIO as GPIO
import sys

command = sys.argv
# for i in range(4):
#     print(i,command[i])

if command[1]=="setup":
    GPIO.setup(command[2],GPIO.OUT)
    p=GPIO.PWM(command[2],5000)
    p.start[0]
    p.ChangeDutyCycle(command[3])
    time.sleep(1)
elif command[1] == "stop":
    GPIO.setup(command[2],GPIO.OUT)
    p=GPIO.PWM(command[2],5000)
    p.stop()
    GPIO.cleanup()
else:
    print("command error!")

# 参数设置：
# 例：python3 pwm_control.py setup 32 20  
# 前两个参数为启动命令，后三个分别是setup或stop、引脚号、空占比
# 命令格式为： python3 pwm_control.py [setup/stop] [PIN] [DutyCycle]

