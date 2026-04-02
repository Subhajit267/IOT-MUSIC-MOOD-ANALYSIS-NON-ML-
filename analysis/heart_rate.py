"""
------------------------------------------------------------
Author: Subhajit Halder
Module: Analysis Layer
File: heart_rate.py

About:
Processes raw MAX30102 sensor data and estimates
heart rate and blood oxygen level.

Revisions:
- 2026-03-12 Added calculate_spo2 function
------------------------------------------------------------
"""

import numpy as np
import time
from sensors.max30102 import read_raw


def collect_samples(count=100):

    ir_values = []
    red_values = []

    for _ in range(count):

        ir, red = read_raw()

        ir_values.append(ir)
        red_values.append(red)

        time.sleep(0.02)

    return np.array(ir_values), np.array(red_values)


def calculate_hr(ir):

    peaks = np.diff(np.sign(np.diff(ir))) < 0
    indices = np.where(peaks)[0]

    if len(indices) < 2:
        return None

    intervals = np.diff(indices)

    mean_interval = np.mean(intervals)

    hr = int(60 / (mean_interval * 0.02))

    if hr < 40 or hr > 200:
        return None

    return hr


def calculate_spo2(ir, red):

    if ir == 0:
        return None

    ratio = red / ir

    spo2 = 110 - 25 * ratio

    spo2 = int(max(90, min(spo2, 100)))

    return spo2


def read_hr_spo2():

    ir, red = collect_samples()

    hr = calculate_hr(ir)

    if hr is None:
        return None, None

    spo2 = calculate_spo2(np.mean(ir), np.mean(red))

    return hr, spo2