from setuptools import setup

setup(
        name='super-termometer',
        version='0.1',
        description='With the help of a DHT22 and a 5 Volts relay we can save energy ' +
                    'in air conditioner that don\'t have an auto shut down function.',

        author='JC_Tec_',
        url='https://github.com/JCTec/SuperTermometer.git',
        packages=['SPLibrary', 'super_termometer', 'dht_read'],
        install_requires=[
            'RPi.GPIO',
            'Adafruit-Blinka',
            'adafruit-circuitpython-dht',
            'Adafruit-PlatformDetect',
            'Adafruit-PureIO',
            'board',
            'pyftdi',
            'pyserial',
            'pyusb'
        ],
        entry_points={
          'console_scripts': [
              'super-termometer = super_termometer.ac_unit:run_ac_unit',
              'dht-read = dht_read.dht_read:run_dht_unit'
          ]
        },
    )

