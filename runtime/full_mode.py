"""
------------------------------------------------------------
Author: Subhajit Halder
Module: Runtime Layer
File: full_mode.py

About:
Full therapy system using real sensors.

Revisions:
- 2026-03-12 Motion stability filter added
------------------------------------------------------------
"""

from sensors.gsr import read_gsr
from sensors.mpu6050 import read_motion
from sensors.motion_filter import is_stable

from analysis.heart_rate import read_hr_spo2
from analysis.stress_detector import detect_stress
from analysis.mood_engine import detect_mood, therapy_target

from therapy.music_player import choose_song, play_song

from utils.display import show_monitor, show_unstable
from utils.helpers import get_timestamp
from utils.logger import log_data, check_and_mark_interruption

def run():

    while True:
        check_and_mark_interruption()

        hr, spo2 = read_hr_spo2()

        gsr_value, voltage = read_gsr()

        motion = read_motion()

        if not is_stable(motion):

            show_unstable(get_timestamp())

            continue

        stress = detect_stress(gsr_value)

        mood = detect_mood(hr, stress)

        target = therapy_target(mood)

        song = choose_song(target)

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

            "music": song.split("/")[-1] if song else "N/A"
        }

        show_monitor(data)
        log_data(data)
        play_song(song)