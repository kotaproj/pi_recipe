from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

# error: 56
# ok: 57
# ok: 58
# ok: 59
# ok: 60
# ok: 61
# ok: 62
# ok: 63
# ok: 64
# ok: 65
# ok: 66
# ok: 67
# ok: 68
# ok: 69
# ok: 70
# ok: 71
# ok: 72
# ok: 73
# ok: 74
# ok: 75
# ok: 76
# ok: 77
# ok: 78
# ok: 79
# ok: 80
# ok: 81
# error: 82

# 実機で確認したところ、
# 厳密な音を



# BUZZERのピン設定
BUZZER_PIN = 18

# ドレミ - 音名 + オクターブで指定
ONPUS = [
    "C4",   # ド
    # "D4",   # レ
    "E4",   # ミ
    # "F4",   # ファ
    "G4",   # ソ
    # "A4",   # ラ
    "B4",   # シ
    # "C5",   # ド
]


def main():
    # 各ピンをbuzzer設定
    factory = PiGPIOFactory()
    buzzer = TonalBuzzer(BUZZER_PIN, pin_factory=factory)

    # 音を鳴らす
    # for note_no in range(0, 128):
    #     try:
    #         buzzer.play(Tone(note_no)) # middle C in MIDI notation
    #         print("ok:", note_no)
    #         sleep(1)
    #     except:
    #         print("error:", note_no)

    # try:

    #     # ドレミ
    #     # for onpu in DOREMI:
    #     #     buzzer.play(Tone(onpu))
    #     #     sleep(0.5)
    #     # buzzer.stop()

    #     for note_no in range(0, 127, 1):
    #         # buzzer.play(Tone(60)) # middle C in MIDI notation
    #         buzzer.play(Tone(note_no)) # middle C in MIDI notation
    #         sleep(1)
    #     # 周波数で指定(1000Hz->1200Hz->...->2000Hz)
    #     # for freq in range(100, 2001, 100):
    #     #     print("freq : ", freq, "Hz")
    #     #     buzzer.play(Tone(frequency=60)) # Hz
    #     #     sleep(1)
    #     buzzer.stop()
    # except:
    #     buzzer.stop()
    #     print("stop")


    # 音を鳴らす
    try:
        # 周波数指定
        for freq in range(300, 400, 100):
            buzzer.play(Tone(frequency=freq))
            sleep(0.5)
        buzzer.stop()
        sleep(0.5)

        # 音符指定
        for onpu in ONPUS:
            buzzer.play(Tone(onpu))
            sleep(0.5)
        buzzer.stop()
        sleep(0.5)

        # midi note指定
        for note_no in range(60, 80, 5):
            buzzer.play(Tone(midi=note_no)) # middle C in MIDI notation
            sleep(0.5)
        buzzer.stop()
        sleep(0.5)

        



    #     for note_no in range(0, 127, 1):
    #         # buzzer.play(Tone(60)) # middle C in MIDI notation
    #         buzzer.play(Tone(note_no)) # middle C in MIDI notation
    #         sleep(1)
    #     # 周波数で指定(1000Hz->1200Hz->...->2000Hz)
    #     # for freq in range(100, 2001, 100):
    #     #     print("freq : ", freq, "Hz")
    #     #     buzzer.play(Tone(frequency=60)) # Hz
    #     #     sleep(1)
    #     buzzer.stop()
    except:
        buzzer.stop()
        print("stop")

    return

if __name__ == "__main__":
    main()