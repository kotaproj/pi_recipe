from gpiozero import MCP3002
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep


def main():

    factory = PiGPIOFactory()
    Vref = 3.3
    adc_ch0 = MCP3002(channel=0, max_voltage=Vref, pin_factory=factory)
    while True:
        print(f'value:{adc_ch0.value:.2f}, Volt:{adc_ch0.value * Vref:.2f}')
        sleep(1)
    return

if __name__ == "__main__":
    main()
