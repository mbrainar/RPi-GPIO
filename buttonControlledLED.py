import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(7,False)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        #print('Button Pressed')
        GPIO.output(7,True)
        time.sleep(0.2)
    else:
	GPIO.output(7,False)
	time.sleep(0.2)

