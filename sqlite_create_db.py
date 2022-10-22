#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sqlite_create_db.py
#  
import sqlite3


def sql_create_db():
    conn = sqlite3.connect('.temp_humid_py.db')  # Opens Connection to SQLite database file.
    conn.execute('\n'
                 '        CREATE TABLE "temp_humidity_co2_voc_readings" (\n'
                 '        "id"	INTEGER NOT NULL,\n'
                 '        "temp"	TEXT NOT NULL,\n'
                 '        "humidity"	TEXT,\n'
                 '        "date_time"	BLOB DEFAULT CURRENT_TIMESTAMP,\n'
                 '        "CO2"	INTEGER,\n'
                 '        "VOC"	INTEGER,\n'
                 '        PRIMARY KEY("id" AUTOINCREMENT)\n'
                 ');\n'
                 '')
    conn.commit()  # Commits the entries to the database
    conn.close()


if __name__ == '__main__':
    sql_create_db()
