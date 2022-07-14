import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
import numpy as np
from drawnow import *

# test ..1
GPIO.setmode(GPIO.BCM) # (BCM 명령어를 사용하면 GPIO 넘버) : (BOARD 명령어를 사용하면 핀 넘버) 
GPIO.setwarnings(False)

TRIG = 8
ECHO = 25
print ("Ultrasonic wave distance")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print ("output initialization")
time.sleep(1)

distance = []
second  = []

def show_plot():
    plt.plot(second,distance,label='distance')
    plt.legend()
    plt.grid()
    plt.xlabel('t(sec)')
    plt.ylabel('distance(cm)') 

try :
    start = 0
    end = 0
    t = 0
    while t >= 0:
        GPIO.output(TRIG,True)
        time.sleep(0.00001)
        GPIO.output(TRIG,False)

        while GPIO.input(ECHO) == 0:
            start = time.time()
        
        while GPIO.input(ECHO) == 1:
            end = time.time()

        check_time = end - start
        dis = check_time * 17000
        print("Distance = %.1f cm" %dis)
        time.sleep(1)
        t = t + 1
        if dis >= 50 :
            dis = 50 

        second = np.append(second, t)
        distance  = np.append(distance,dis)

        drawnow(show_plot)



except KeyboardInterrupt:
    print("Complete mesuring")
    GPIO.cleanup()
