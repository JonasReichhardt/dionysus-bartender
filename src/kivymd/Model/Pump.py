import json
import threading
import time

debug = 0

import platform

platformInfo = platform.uname()
if platformInfo.system == 'Linux' and platformInfo.machine.find('64') == -1:
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)
    for p in range(1, 37):
        GPIO.setup(p, GPIO.OUT)
    print(f'\033[93m[INF] GPIO setup done \033[0m')
    debug = 1
else:
    print(f'\033[93m[WRN] not running on raspberry -> no GPIO \033[0m')


class Pump:
    def __init__(self, pins, ingredient, flowrate):
        self.ingredient = ingredient
        self.pins = pins
        self.flowrate = flowrate

    def turnOn(self, timer):
        if (debug == 1):
            GPIO.output(self.pins[0], GPIO.HIGH)
        else:
            print(f'\033[93m[INF] gpio {self.pins[0]} | high\033[0m')
        timer.start()

    def turnOff(self):
        if (debug == 1):
            GPIO.output(self.pins[0], GPIO.LOW)
        else:
            print(f'\033[93m[INF] gpio {self.pins[0]} | low\033[0m')

    def activate(self, amount):
        seconds = amount / self.flowrate
        timer = threading.Timer(seconds, self.turnOff)
        self.turnOn(timer)

    def activate_blocking(self, amount):
        seconds = amount / self.flowrate
        if (debug == 1):
            GPIO.output(self.pins[0], GPIO.HIGH)
        else:
            print(f'\033[93m[INF] gpio {self.pins[0]} | high\033[0m')
        time.sleep(seconds)
        if (debug == 1):
            GPIO.output(self.pins[0], GPIO.LOW)
        else:
            print(f'\033[93m[INF] gpio {self.pins[0]} | low\033[0m')


class PumpFactory:
    def __init__(self, file):
        self.file = file

    def loadFromFile(self):
        with open(self.file) as data:
            pumps = json.load(data)["pumps"]
            data = []
            for pump in pumps:
                pins = pump["pins"]
                ingredient = pump["ingredient"]
                flowrate = pump["flowrate"]
                data.append(Pump(pins, ingredient, flowrate))
            return data
