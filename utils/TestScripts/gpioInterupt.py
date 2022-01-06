# External module imports
import signal                   
import sys
import os
import RPi.GPIO as GPIO

uid = os.getuid()

print("UID = %s"%(uid))

print("Here we go! Press CTRL+C to exit")

BUTTON_GPIO = 11
#LED_GPIO = 20

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)
conta = 0
def button_callback(channel):
    global conta
    if GPIO.input(BUTTON_GPIO):
        conta += 1
        print("Ligou %d vezes"%conta)
    else:
        print("Desligou")

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD) # BOARD pin-numbering scheme
    
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(BUTTON_GPIO, GPIO.RISING, 
            callback=button_callback, bouncetime=100)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()


