import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
import numpy as np

# test ..
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

d = []

try :
    start = 0
    end = 0
    sec = 0
    while sec <= 10:
        GPIO.output(TRIG,True)
        time.sleep(0.00001)
        GPIO.output(TRIG,False)

        while GPIO.input(ECHO) == 0:
            start = time.time()
        
        while GPIO.input(ECHO) == 1:
            end = time.time()

        check_time = end - start
        distance = check_time * 17000
        print("Distance = %.1f cm" %distance)
        time.sleep(1)
        d.append(distance)
        sec = sec + 1

except KeyboardInterrupt:
    print("Complete mesuring")
    GPIO.cleanup()

# t  = np.arange(0,10,1)
# d1 = np.d

# fig, ax = plt.subplot()
# ax.plot(t,d1)

# ax.set(xlabel = 'time (s)', ylabel = 'distance (cm)',
# title = 'Ultrasonic wave distance mesure')
# ax.grid()

# fig.savefig("test2,png")
# plt.show()