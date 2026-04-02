"""
------------------------------------------------------------
Author: Subhajit Halder
Module: Sensor Layer
File: gsr.py

About:
Reads galvanic skin response values using ADS1115 ADC.

------------------------------------------------------------
"""

import board
import busio

import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1115(i2c)

channel = AnalogIn(ads, ADS.P0)


def read_gsr():

    raw_value = channel.value
    voltage = channel.voltage

    return raw_value, voltage