from SPLibrary.common import log
import RPi.GPIO as GPIO
import adafruit_dht
import board
import time

DHT_SENSOR = adafruit_dht.DHT22(board.D4)
AC_PIN = 24
HUMIDIFIER_PIN = 23


def set_up_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(AC_PIN, GPIO.OUT)
    GPIO.setup(HUMIDIFIER_PIN, GPIO.OUT)


def set_grow_room_state(temperature, humidity):
    if temperature < 26.5:
        print("Turning down AC")
        GPIO.output(AC_PIN, GPIO.HIGH)
    elif 26.5 <= temperature < 27.5:
        print("Ideal temperature")
    elif temperature > 27.5:
        print("Turning on AC")
        GPIO.output(AC_PIN, GPIO.LOW)

    time.sleep(0.5)

    if humidity < 60.0:
        print("Turning on Humidifier")
        GPIO.output(HUMIDIFIER_PIN, GPIO.LOW)
    else:
        print("Turning off Humidifier")
        GPIO.output(HUMIDIFIER_PIN, GPIO.HIGH)


def run_ac_unit():
    try:
        set_up_gpio()

        while True:
            try:
                temperature = DHT_SENSOR.temperature
                humidity = DHT_SENSOR.humidity

                if humidity is not None and temperature is not None:
                    log(temperature, humidity)
                    set_grow_room_state(temperature, humidity)
                else:
                    print("Failed to retrieve data from humidity sensor.")

                time.sleep(10)

            except RuntimeError as error:
                print(error.args[0])
                time.sleep(2.0)
                continue

    except KeyboardInterrupt:
        exit_system()

    except Exception as e:
        exit_system()


def exit_system():
    DHT_SENSOR.exit()

    print("")
    print("Exiting SuperTermometer System.")
    time.sleep(1.0)

