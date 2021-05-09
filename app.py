#!/usr/bin/env python3

import RPi.GPIO as GPIO
from subprocess import check_output
from time import sleep


# GPIO pin where you connected base of transisotor. For reference please look at https://www.raspberrypi.org/documentation/usage/gpio/
FAN_CONTROL_PIN_NUMBER = 21

TEMP_WHEN_FAN_TURNS_ON_IN_CELSIUS = 55.0
TEMP_WHEN_FAN_TURNS_OFF_IN_CELSIUS = 50.0
TEMP_CHECK_INTERVAL_IN_SECONDS = 10


def get_cpu_temp():
    def __get_temp__internal():
        out = check_output(["/opt/vc/bin/vcgencmd", "measure_temp"])
        return float(out.split('=')[1].split('\'')[0])
    try:
        return __get_temp__internal()
    except:
        return None


def turn_off_fan():
    GPIO.output(FAN_CONTROL_PIN_NUMBER, False)


def turn_on_fan():
    GPIO.output(FAN_CONTROL_PIN_NUMBER, True)


def setup_fan():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FAN_CONTROL_PIN_NUMBER, GPIO.OUT)
    GPIO.output(FAN_CONTROL_PIN_NUMBER, False)


def main():
    fan_on = False
    setup_fan()
    while True:
        temp = get_cpu_temp()
        if temp:
            if fan_on and temp < TEMP_WHEN_FAN_TURNS_OFF_IN_CELSIUS:
                turn_off_fan()
                fan_on = False
            if (not fan_on) and temp > TEMP_WHEN_FAN_TURNS_ON_IN_CELSIUS:
                turn_on_fan()
                fan_on = True
        # if unknown state turn on fan
        elif not fan_on:
            turn_on_fan()
            fan_on = True
        sleep(TEMP_CHECK_INTERVAL_IN_SECONDS)


sleep(TEMP_CHECK_INTERVAL_IN_SECONDS)
main()
