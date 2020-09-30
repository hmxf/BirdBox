import pigpio
import time

pi=pigpio.pi()
pi.set_mode(32, pigpio.OUTPUT)
pi.set_PWM_frequency(32,5000)
pi.set_PWM_range(32,1000)
pi.set_PWM_dutycycle(32,100)
time.sleep(5)
pi.set_PWM_dutycycle(32,50)
time.sleep(5)