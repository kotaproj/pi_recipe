import sys
import time
from gpiozero import OutputDevice
from gpiozero.pins.pigpio import PiGPIOFactory

# pin settings
RELAY_PIN_0 = 21

def main():
    # use pigpio
    factory = PiGPIOFactory()
    tap_pin = OutputDevice(RELAY_PIN_0, pin_factory=factory)

    args = sys.argv
    count = int(args[1])

    # tap
    for _ in range(count):
        tap_pin.on()
        time.sleep(0.050)
        tap_pin.off()
        time.sleep(0.050)
    return


if __name__ == "__main__":
    main()