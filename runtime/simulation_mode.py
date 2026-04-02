"""
------------------------------------------------------------
Author: Subhajit Halder
Module: Runtime Layer
File: simulation_mode.py

About:
Runs monitoring pipeline using CSV dataset.

Revisions:
- 2026-03-12 Motion stability filter added
------------------------------------------------------------
"""

import csv

from sensors.motion_filter import is_stable

from analysis.mood_engine import detect_mood, therapy_target

from therapy.music_player import choose_song, play_song

from utils.display import show_monitor, show_unstable
from utils.helpers import get_timestamp

DATA_FILE = "data/simulation_data.csv"


def run():

    with open(DATA_FILE) as f:

        reader = csv.DictReader(f)

        for row in reader:

            motion = int(row["motion"])

            if not is_stable(motion):

                show_unstable(get_timestamp())

                continue

            hr = int(row["hr"])

            stress = row["stress"]

            mood = detect_mood(hr, stress)

            target = therapy_target(mood)

            song = choose_song(target)

            data = {

                "timestamp": get_timestamp(),

                "ir": int(row["ir"]),
                "red": int(row["red"]),
                "gsr_voltage": float(row["gsr_voltage"]),
                "motion": motion,

                "hr": hr,
                "spo2": int(row["spo2"]),
                "gsr": int(row["gsr"]),

                "motion_state": "SIMULATED",

                "stress": stress,
                "mood": mood,

                "target": target,

                "music": song.split("/")[-1] if song else "N/A"
            }

            show_monitor(data)

            play_song(song)