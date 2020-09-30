import pigpio
import time

pi = pigpio.pi()
pi2 = pigpio.pi()
pi.set_PWM_frequency(23, 50)  # frequency 50Hz
pi.set_PWM_range(23, 1000)    # set range 1000
# pi.set_PWM_dutycycle(23, 800)  # set an initial position
pi2.set_PWM_frequency(25, 50)  # frequency 50Hz
pi2.set_PWM_range(25, 1000)    # set range 1000
# pi2.set_PWM_dutycycle(25, 800)  # set an initial position
# time.sleep(2)                 # wait for 2 seconds

# BCM 编号
# LED 12
# FAN1 23
# FAN2 25
# SERVO 12

delay = 1
# while True:
#     pi.set_PWM_dutycycle(23, 10)  # 2.5%
#     time.sleep(delay)
#     pi.set_PWM_dutycycle(23, 800) # 23.5%
#     time.sleep(delay)

pi_led = pigpio.pi()
pi_led.set_PWM_frequency(12, 5000)  # frequency 50Hz
pi_led.set_PWM_range(12, 1000)    # set range 1000
# pi_led.set_PWM_dutycycle(12, 25)  # set an initial position
# time.sleep(10)

pi_servo = pigpio.pi()
# pi_servo.set_servo_pulsewidth(20, 1500) # centre
print("舵机 风扇 LED")
while True:
    print(" 左   低   暗")
    pi_servo.set_servo_pulsewidth(20, 500) # centre
    time.sleep(delay)
    pi.set_PWM_dutycycle(23, 200)  # set an initial position
    time.sleep(delay)
    pi2.set_PWM_dutycycle(25, 200)  # set an initial position
    time.sleep(delay)
    pi_led.set_PWM_dutycycle(12, 25)  # set an initial position
    time.sleep(delay)
    print(" 中   中   中")
    pi_servo.set_servo_pulsewidth(20, 1500) # centre
    time.sleep(delay)
    pi.set_PWM_dutycycle(23, 500)  # set an initial position
    time.sleep(delay)
    pi2.set_PWM_dutycycle(25, 500)  # set an initial position
    time.sleep(delay)
    pi_led.set_PWM_dutycycle(12, 45)  # set an initial position
    time.sleep(delay)
    print(" 右   高   亮")
    pi_servo.set_servo_pulsewidth(20, 2500) # centre
    time.sleep(delay)
    pi.set_PWM_dutycycle(23, 800)  # set an initial position
    time.sleep(delay)
    pi2.set_PWM_dutycycle(25, 800)  # set an initial position
    time.sleep(delay)
    pi_led.set_PWM_dutycycle(12, 65)  # set an initial position

    time.sleep(3)