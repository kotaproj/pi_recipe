from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

# LEDのピン設定
PIN_LED1 = 21

def main():
    # LEDピン設定
    factory = PiGPIOFactory()
    led = LED(PIN_LED1, pin_factory=factory)

    # LEDをチカチカ
    for _ in range(5):
        print("LED ON")
        led.on()
        sleep(0.5)
        print("LED OFF")
        led.off()
        sleep(0.5)

    # blinkを使用することも可能
    print("blink")
    led.blink()
    sleep(3)
    led.off()

    # toggleを使用することも可能
    print("toggle")
    for _ in range(20):
        led.toggle()
        sleep(0.1)

if __name__ == "__main__":
    main()