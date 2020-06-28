#coding=utf-8
import pigpio
import time
import sys
command = sys.argv

if command[1]=='-h':
    print('''
Example: python3 pwm_control.py [PIN] [DutyCycle] [Types]

Types: LED,FAN,SERVO

BCM Number:
LED 12
FAN1 23
FAN2 25
SERVO 20
''')
    sys.exit()
pin = int(command[1])
duty = int(command[2])
types = command[3]
if types == 'LED':
    fc = 5000
    if duty>80 or duty<25:
        print("LED error!")
        sys.exit()
elif types =='FAN':
    fc = 50
    if duty>1000 or duty<0:
        print("LED error!")
        sys.exit()
else:
    fc = 50
    if duty>90 or duty<-90:
        print("SERVO error")
        sys.exit()

if types != 'SERVO':
    pi = pigpio.pi()
    pi.set_PWM_frequency(pin,5000)
    pi.set_PWM_range(pin,1000)
    pi.set_PWM_dutycycle(pin,duty)
    time.sleep(0.5)
else :
    pi = pigpio.pi()
    pi.set_servo_pulsewidth(pin,1500+duty/90*1000)


# 命令格式为： python3 pwm_control.py [PIN] [DutyCycle] [types]
# types: LED,FAN,SERVO
# 1500+x/90*1000