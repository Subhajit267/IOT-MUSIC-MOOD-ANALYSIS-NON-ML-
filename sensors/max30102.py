"""
------------------------------------------------------------
Author: Subhajit Halder
Module: Sensor Layer
File: max30102.py

About:
Low level driver for MAX30102 pulse sensor.

------------------------------------------------------------
"""

from smbus2 import SMBus

bus = SMBus(1)

ADDR = 0x57


def read_raw():

    try:

        data = bus.read_i2c_block_data(ADDR, 0x07, 6)

        red = (data[0] << 16) | (data[1] << 8) | data[2]
        ir = (data[3] << 16) | (data[4] << 8) | data[5]

        return ir, red

    except:

        return 0, 0