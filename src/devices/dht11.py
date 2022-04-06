import logging

import RPi.GPIO as GPIO
import dht11


def dht11():
    try:
        # initialize GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()

        # read data using pin 14
        instance = dht11.DHT11(pin=4)
        result = instance.read()

        if result.is_valid():
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
            return result.temperature, result.humidity
        else:
            print("Error: %d" % result.error_code)
            return 0, 0

    except Exception as e:
        logging.DEBUG(f'{e}')
        return 0, 0
