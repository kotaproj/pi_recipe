from gpiozero import OutputDevice
from gpiozero import InputDevice
from gpiozero.pins.pigpio import PiGPIOFactory

import time

# HC SR04の使用するピン
PIN_TRIG = 22
PIN_ECHO = 27

def main():
    # ピン設定
    factory = PiGPIOFactory()
    pin_trig = OutputDevice(PIN_TRIG, pin_factory=factory)
    pin_echo = InputDevice(PIN_ECHO, pin_factory=factory)
    pin_trig.off()
    time.sleep(0.3)

    # 計測
    pin_trig.on()
    time.sleep(0.00001)
    pin_trig.off()

    # 計測 - 反射までの時間を取得
    while pin_echo.value == 0:
        signal_low = time.time()

    while pin_echo.value == 1:
        signal_high = time.time()

    # 結果表示
    time_delta = signal_high - signal_low
    distance = time_delta * 17000

    print("distance:", distance, "cm")

if __name__ == "__main__":
    main()