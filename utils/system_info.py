"""
------------------------------------------------------------
Author: Subhajit Halder
Module: Utility Layer
File: system_info.py

About:
Detects hardware sensors via I2C.

Revisions:
- 2026-03-12 Hardware detection fix
------------------------------------------------------------
"""

from smbus2 import SMBus


def check(addr):

    try:
        bus = SMBus(1)
        bus.read_byte(addr)
        return True
    except:
        return False


def sensors_available():

    return check(0x57) and check(0x68) and check(0x48)


def system_info():

    print("\n----------- SENSOR STATUS -----------")

    print("MAX30102 :", "CONNECTED-ONLINE" if check(0x57) else "NOT FOUND")
    print("MPU6050  :", "CONNECTED-ONLINE" if check(0x68) else "NOT FOUND")
    print("ADS1115  :", "CONNECTED-ONLINE" if check(0x48) else "NOT FOUND")

    print("-------------------------------------")