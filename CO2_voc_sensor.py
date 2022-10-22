# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# """ Example for using the SGP30 with CircuitPython and the Adafruit library"""

import time
import board
import busio
import adafruit_sgp30
import adafruit_ahtx0
import sqlite_updatedb_module
from datetime import datetime


# sgp30.set_iaq_baseline(0x8973, 0x8AAE)
# sgp30.set_iaq_relative_humidity(celsius=temp_sensor.temperature, relative_humidity=temp_sensor.relative_humidity)


def voc_temp_humid():
    global print
    elapsed_sec = 0
    while True:
        print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))
        time.sleep(1)
        elapsed_sec += 1
        if elapsed_sec > 10:
            elapsed_sec = 0
            print(f"**** Baseline values: eCO2 = {int(sgp30.baseline_eCO2)}, TVOC = {int(sgp30.baseline_TVOC)}")

            # "**** Baseline values: eCO2 = 0x%x, TVOC = 0x%x" % (sgp30.baseline_eCO2, sgp30.baseline_TVOC))
            updated_temp_c = temp_sensor.temperature
            updated_temp_f = convert_to_f(updated_temp_c)
            updated_humid = temp_sensor.relative_humidity
            print(f"Updating temp to {updated_temp_f}F and humidity of {int(updated_humid)}%")
            #         update the VOC sensor with current temp/humid
            sgp30.set_iaq_relative_humidity(celsius=updated_temp_c, relative_humidity=updated_humid)
            # record to the database
            dt_now = datetime.now()
            format_dt_now = dt_now.strftime(dt_string)
            sqlite_updatedb_module.update_temp_humid_reading(updated_temp_f, int(updated_humid),
                                                             sgp30.eCO2, sgp30.TVOC, format_dt_now)


def convert_to_f(temp_c):
    temp_f = (temp_c * 9 / 5) + 32
    return int(temp_f)


if __name__ == '__main__':
    # formate date/time information
    dt_string = "%Y/%m/%d %H:%M:%S"

    # Create the sensor object using I2C Temp / Humid
    temp_sensor = adafruit_ahtx0.AHTx0(board.I2C())

    # Create a sensor object for the VOC
    i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)

    # Create library object on our I2C port
    sgp30 = adafruit_sgp30.Adafruit_SGP30(board.I2C())
    # sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

    # print("AHT status: ", [hex(i) for i in temp_sensor.i2c_device])
    # print("SGP30 serial #", [hex(i) for i in sgp30.serial])

    voc_temp_humid()
