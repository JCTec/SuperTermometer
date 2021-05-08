import time


def log(temperature, humidity):
    print('{0} {1}: {2:0.1f}C {3:0.1f}%'.format(time.strftime('%m/%d/%y'),
                                                time.strftime('%H:%M'),
                                                temperature,
                                                humidity))

