from gpiozero import MCP3002
from gpiozero.pins.pigpio import PiGPIOFactory

from time import sleep

# SWのピン設定
PIN_BTN1 = 5

def main():

    factory = PiGPIOFactory()
    Vref = 3.3
    adc_ch0 = MCP3002(channel=0, max_voltage=Vref, pin_factory=factory)
    while True:
        print(adc_ch0.value * Vref, adc_ch0.value)
        # print(adc_ch0.value * Vref)
        sleep(1)
    return

if __name__ == "__main__":
    main()
