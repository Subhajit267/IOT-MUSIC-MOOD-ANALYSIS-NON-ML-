"""
------------------------------------------------------------
Author: Subhajit Halder
Module: Sensor Layer
File: mpu6050.py

About:
Reads accelerometer values from MPU6050
to determine motion stability.

------------------------------------------------------------
"""

from smbus2 import SMBus
import math

bus = SMBus(1)
ADDR = 0x68

def read_word(reg):

    high = bus.read_byte_data(ADDR, reg)
    low = bus.read_byte_data(ADDR, reg + 1)

    value = (high << 8) + low

    if value >= 0x8000:
        value = -((65535 - value) + 1)

    return value

def read_motion():

    ax = read_word(0x3B)
    ay = read_word(0x3D)
    az = read_word(0x3F)

    motion = math.sqrt(ax * ax + ay * ay + az * az)

    return motion