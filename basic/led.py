from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

# LEDのピン設定
PIN_LED1 = 16

def main():
    # LEDピン設定
    factory = PiGPIOFactory()
    led = LED(PIN_LED1, pin_factory=factory)

    # LEDをチカチカ
    try:
        for _ in range(5):
            print("LED ON")
            led.on()
            sleep(0.5)
            print("LED OFF")
            led.off()
            sleep(0.5)
    except KeyboardInterrupt:
        print("stop")


if __name__ == "__main__":
    main()