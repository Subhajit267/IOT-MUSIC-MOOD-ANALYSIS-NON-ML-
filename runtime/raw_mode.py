"""
------------------------------------------------------------
Author: Subhajit Halder
Module: Runtime Layer
File: raw_mode.py

About:
Displays real sensor data every 5 seconds.
Music playback disabled.

Revisions:
- 2026-03-12 Motion stability check added
------------------------------------------------------------
"""

import time

from sensors.gsr import read_gsr
from sensors.mpu6050 import read_motion
from sensors.motion_filter import is_stable

from analysis.heart_rate import read_hr_spo2
from analysis.stress_detector import detect_stress
from analysis.mood_engine import detect_mood, therapy_target

from utils.display import show_monitor, show_unstable
from utils.helpers import get_timestamp


def run():

    while True:

        hr, spo2 = read_hr_spo2()

        gsr_value, voltage = read_gsr()

        motion = read_motion()

        if not is_stable(motion):

            show_unstable(get_timestamp())

            time.sleep(5)

            continue

        stress = detect_stress(gsr_value)

        mood = detect_mood(hr, stress)

        target = therapy_target(mood)

        data = {

            "timestamp": get_timestamp(),

            "ir": "MEASURED",
            "red": "MEASURED",
            "gsr_voltage": round(voltage, 2),
            "motion": motion,

            "hr": hr,
            "spo2": spo2,
            "gsr": gsr_value,

            "motion_state": "STABLE",

            "stress": stress,
            "mood": mood,

            "target": target,

            "music": "N/A"
        }

        show_monitor(data)

        time.sleep(5)