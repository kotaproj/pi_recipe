from gpiozero import DistanceSensor
from gpiozero import LED
from signal import pause
from gpiozero.pins.pigpio import PiGPIOFactory

import time

# HC SR04の使用するピン
PIN_TRIG = 22
PIN_ECHO = 27

# LEDで使用するピン
PIN_LED1 = 21

def main():
    # ピン設定
    factory = PiGPIOFactory()
    # sensor = DistanceSensor(PIN_ECHO, PIN_TRIG, max_distance=1, threshold_distance=0.2, pin_factory=factory)
    # sensor = DistanceSensor(PIN_ECHO, PIN_TRIG, max_distance=1, threshold_distance=0.3, pin_factory=factory)
    sensor = DistanceSensor(PIN_ECHO, PIN_TRIG, max_distance=1, threshold_distance=0.7, pin_factory=factory)
    # sensor = DistanceSensor(PIN_ECHO, PIN_TRIG, max_distance=1, threshold_distance=0.4, pin_factory=factory)
    led = LED(PIN_LED1, pin_factory=factory)

    sensor.when_in_range = led.on
    sensor.when_out_of_range = led.off
    pause()

if __name__ == "__main__":
    main()