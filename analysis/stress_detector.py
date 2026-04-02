"""
------------------------------------------------------------
Author: Subhajit Halder
Module: Analysis Layer
File: stress_detector.py

About:
Converts galvanic skin response (GSR) values
into stress level categories.

------------------------------------------------------------
"""

from config.settings import GSR_HIGH, GSR_MEDIUM


def detect_stress(gsr):

    if gsr > GSR_HIGH:
        return "VERY HIGH"

    elif gsr > GSR_MEDIUM:
        return "HIGH"

    elif gsr > 14000:
        return "MEDIUM"

    else:
        return "LOW"