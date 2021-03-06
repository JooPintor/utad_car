# External module imports
import RPi.GPIO as GPIO
import time
import os

uid = os.getuid()

print("UID = %s"%(uid))

#os.setuid(0)

# Pin Definitons:
#pwmPin = 18 # Broadcom pin 18 (P1 pin 12)
#ledPin = 23 # Broadcom pin 23 (P1 pin 16)
butPin = 11 # Broadcom pin 17 (P1 pin 11)

#dc = 95 # duty cycle (0-100) for PWM pin

# Pin Setup:
#GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setmode(GPIO.BOARD) # BOARD pin-numbering scheme
#GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output
#GPIO.setup(pwmPin, GPIO.OUT) # PWM pin set as output
#pwm = GPIO.PWM(pwmPin, 50)  # Initialize PWM on pwmPin 100Hz frequency
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Button pin set as input w/ pull-up

# Initial state for LEDs:
#GPIO.output(ledPin, GPIO.LOW)
#pwm.start(dc)

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        if GPIO.input(butPin): # button is released
#            pwm.ChangeDutyCycle(dc)
#            GPIO.output(ledPin, GPIO.LOW)
            print("Ligado")
            time.sleep(1.0)
        else: # button is pressed:
#            pwm.ChangeDutyCycle(100-dc)
#            GPIO.output(ledPin, GPIO.HIGH)
#            GPIO.output(ledPin, GPIO.LOW)
            print("Desligado")
            time.sleep(1.0)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
#    pwm.stop() # stop PWM
    GPIO.cleanup() # cleanup all GPIO
