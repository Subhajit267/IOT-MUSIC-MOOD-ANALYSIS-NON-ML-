"""
------------------------------------------------------------
Author: Subhajit Halder
Module: Sensor Layer
File: motion_filter.py

About:
Checks motion stability using MPU6050 magnitude.
------------------------------------------------------------
"""

from config.settings import MOTION_THRESHOLD


def is_stable(motion):

    if motion > MOTION_THRESHOLD:
        return False

    return True