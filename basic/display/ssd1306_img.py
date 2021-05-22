
# 4rc:~/pi_recipe/basic $ sudo apt-get install fonts-noto
# pe/basic $ sudo apt-get install fonts-ipafont

import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# SSD1306のピン設定
DEVICE_ADR = 0x3C
DISP_WIDTH = 128
DISP_HEIGHT = 64

def main():

    # Setting some variables for our reset pin etc.
    RESET_PIN = digitalio.DigitalInOut(board.D4)

    # Very important... This lets py-gaugette 'know' what pins to use in order to reset the display
    i2c = board.I2C()
    oled = adafruit_ssd1306.SSD1306_I2C(DISP_WIDTH, DISP_HEIGHT, i2c, addr=DEVICE_ADR, reset=RESET_PIN)

    # Clear display.
    oled.fill(0)
    oled.show()

    # Create blank image for drawing.
    image = Image.open("graph.png")
    draw = ImageDraw.Draw(image)

    # Display image
    oled.image(image)
    oled.show()
    return

if __name__ == "__main__":
    main()
