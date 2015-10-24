import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
p17 = GPIO.PWM(17,50)
dc = 95
p17.start(dc)

print 'Here we go! Press CTRL+C to quit.'
try:
    while True:
        p17.ChangeDutyCycle(5)

        # sleep(1)
        # p17.ChangeDutyCycle(12.5)
        # sleep(1)
        # p17.ChangeDutyCycle(2.5)
        # sleep(1)
except KeyboardInterrupt:
    p17.stop()
    GPIO.cleanup()
    print 'See ya later!'
    
