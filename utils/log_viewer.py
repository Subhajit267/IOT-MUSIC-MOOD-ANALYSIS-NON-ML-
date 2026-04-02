"""
------------------------------------------------------------
Author: Subhajit Halder
Module: Utility Layer
File: log_viewer.py

About:
Displays previously recorded physiological data
stored in the CSV log file.

------------------------------------------------------------
"""

import csv

LOG_FILE = "data/logs/mood_log.csv"


def view_logs():

    try:

        with open(LOG_FILE) as f:

            reader = csv.DictReader(f)

            for row in reader:

                print(row)

    except FileNotFoundError:

        print("No logs available")