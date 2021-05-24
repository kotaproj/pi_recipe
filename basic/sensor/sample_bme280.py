from bme280 import bme280
from bme280 import bme280_i2c

def main():
    # 初期化
    bme280_i2c.set_default_i2c_address(0x76)
    bme280_i2c.set_default_bus(1)

    # キャリブレーション
    bme280.setup()

    # データ取得
    data_all = bme280.read_all()

    # 温度、湿度、気圧の表示
    print("%7.2f hPa" % data_all.pressure)
    print("%7.2f %%" % data_all.humidity)
    print("%7.2f C" % data_all.temperature)
    return

if __name__ == "__main__":
    main()
