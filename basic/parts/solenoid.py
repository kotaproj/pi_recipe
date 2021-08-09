import sys
import time
from gpiozero import OutputDevice
from gpiozero.pins.pigpio import PiGPIOFactory

# pin settings
SOLENOID_PIN_0 = 21

def main():
    # use pigpio
    factory = PiGPIOFactory()
    sole_pin = OutputDevice(SOLENOID_PIN_0, pin_factory=factory)

    args = sys.argv
    count = int(args[1])

    # pull/push
    for _ in range(count):
        sole_pin.on()
        time.sleep(0.100)
        sole_pin.off()
        time.sleep(0.100)
    return


if __name__ == "__main__":
    main()
