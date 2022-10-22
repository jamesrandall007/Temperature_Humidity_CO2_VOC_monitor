#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sqlite_updatedb_module
#  
import sqlite3


def update_temp_humid_reading(temperature, humidity, CO2, VOC, date_time='None'):
    conn = sqlite3.connect('temp_humid_py.db')
    cursor = conn.cursor()
    readings = (temperature, humidity, CO2, VOC, date_time)
    cursor.execute("INSERT INTO temp_humidity_co2_voc_readings (temp, humidity, CO2, VOC, date_time) VALUES ( ?, ?, ?, ?, ?)", readings)
    conn.commit()
    conn.close()
    # return f"Updated {temperature: .1f} degrees and Humidity: {humidity: .1f} % \n at {date_time}"
    return 'updated'


if __name__ == '__main__':
    update_temp_humid_reading(15.5, 75, 400, 3500)
