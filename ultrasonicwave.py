import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # (BCM 명령어를 사용하면 GPIO 넘버) : (BOARD 명령어를 사용하면 핀 넘버) 
GPIO.setwarnings(False)

TRIG = 8
ECHO = 9
print ("Ultrasonic wave distance")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print ("output initialization")
time.sleep(1)

try :
    start = 0
    end = 0
    while True:
        GPIO.output(TRIG,True)
        time.sleep(0.00001)
        GPIO.output(TRIG,False)

        while GPIO.input(ECHO) == 0:
            start = time.time()
            print(start)
        
        while GPIO.input(ECHO) == 1:
            end = time.time()
            print(end)

        check_time = end - start
        print(check_time)
        distance = check_time * 17000
        print("Distance = %.1f cm" %distance)
        time.sleep(0.4)

except KeyboardInterrupt:
    print("Complete mesuring")
    GPIO.cleanup()