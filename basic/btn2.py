from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory
from signal import pause

# SWのピン設定
PIN_BTN1 = 5

def main():
    # SWピンを入力に設定(プルアップ設定)
    factory = PiGPIOFactory()
    btn = Button(PIN_BTN1, pull_up=True, pin_factory=factory)

    def press_btn():
        print("pressed button!")

    def release_btn():
        print("released button!")

    btn.when_pressed = press_btn
    btn.when_released = release_btn
    pause()

    return

if __name__ == "__main__":
    main()