import RPi.GPIO as GPIO
import time

class OutputWriter():


    def pinON(self,outputPin):
        GPIO.output (outputPin, GPIO.LOW)

    def pinOFF(self,outputPin):
        GPIO.output (outputPin, GPIO.HIGH)


    def setup(self,outputPin):
        GPIO.setmode (GPIO.BCM)  # Numbers GPIOs by BCM
        GPIO.setup (outputPin, GPIO.OUT)  # Set LedPin's mode is output
        GPIO.output (outputPin, GPIO.HIGH)  # Set LedPin high(+3.3V) to off led


 
