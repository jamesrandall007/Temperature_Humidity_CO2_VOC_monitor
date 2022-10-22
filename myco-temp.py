import sqlite_updatedb_module
import time
from icecream import ic
from datetime import datetime
import sqlite3
import board
import adafruit_ahtx0

# Create the sensor object using I2C
sensor = adafruit_ahtx0.AHTx0(board.I2C())

# formate date/time information
dt_string = "%Y/%m/%d %H:%M:%S"


def convert_to_f(temp_c):
    temp_f = (temp_c * 9 / 5) + 32
    return temp_f


while True:
    temp_sensor = sensor.temperature
    humidity_sensor = sensor.relative_humidity

    print("Temp F:", int(convert_to_f(temp_sensor)), "  Humidity: ", int(humidity_sensor))

    dt_now = datetime.now().strftime(dt_string)
    # ic(datetime.now().strftime(dt_string))
    # ic(sqlite_updatedb_module.update_temp_humid_reading(temp_sensor, humidity_sensor, dt_now))
    sqlite_updatedb_module.update_temp_humid_reading(temp_sensor, humidity_sensor, dt_now)
    time.sleep(60)
