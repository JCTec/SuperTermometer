from SPLibrary.common import log
import adafruit_dht
import board
import time

DHT_SENSOR = adafruit_dht.DHT22(board.D4)


def run_dht_unit():
    try:
        read_dht = True

        while read_dht:
            try:
                temperature = DHT_SENSOR.temperature
                humidity = DHT_SENSOR.humidity

                if humidity is not None and temperature is not None:
                    read_dht = False
                    log(temperature, humidity)
                else:
                    print("Failed to retrieve data from humidity sensor.")

                if read_dht:
                    time.sleep(2.0)

            except RuntimeError as error:
                print(error.args[0])
                time.sleep(2.0)
                continue

    except Exception as e:
        DHT_SENSOR.exit()
        print("Exiting DHT Read.")

