import os
import time
import Adafruit_DHT
import RPi.GPIO as GPIO

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
RELAY_PIN = 18

LAST_TEMP = None


def set_up_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RELAY_PIN, GPIO.OUT)


def set_relay_state(temperature):
    print(abs(LAST_TEMP - temperature))

    if abs(LAST_TEMP - temperature) < 5.0:
        if temperature < 26.5:
            GPIO.output(RELAY_PIN, GPIO.LOW)
        elif 26.5 <= temperature < 27.5:
            print("Ideal temperature")
        elif temperature > 27.5:
            GPIO.output(RELAY_PIN, GPIO.HIGH)
    else:
        print("Too high absolute difference.")
        print(abs(LAST_TEMP - temperature))


def get_log_file():
    try:
        f = open('/home/pi/humidity.csv', 'a+')
        if os.stat('/home/pi/humidity.csv').st_size == 0:
            f.write('Date,Time,Temperature,Humidity\r\n')

        return f
    except Exception as e:
        print("Failed opening file.")
        return None


def log_temperature(file, temperature, humidity):
    file.write('{0},{1},{2:0.1f}*C,{3:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'),
                                                         time.strftime('%H:%M'),
                                                         temperature, humidity))

try:
    set_up_gpio()

    file = get_log_file()

    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        if humidity is not None and temperature is not None:
            log_temperature(file, temperature, humidity)

            if LAST_TEMP is None:
                LAST_TEMP = temperature

            set_relay_state(temperature)
        else:
            print("Failed to retrieve data from humidity sensor.")

        time.sleep(30)
except Exception as e:
    print("Exiting SuperTermometer System.")

