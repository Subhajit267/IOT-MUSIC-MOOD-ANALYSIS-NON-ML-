"""
------------------------------------------------------------
Author: Subhajit Halder
Module: Utility Layer
File: logger.py

About:
Stores system measurements into CSV format
for later analysis.

Revisions:
- 2026-03-12 Initial implementation
- 2026-04-02 Added interruption handling
- 2026-04-02 Added session separation
------------------------------------------------------------
"""

import csv
import os

LOG_FILE = "data/logs/mood_log.csv"


def add_blank_line():

    with open(LOG_FILE, "a") as f:
        f.write("\n")


def check_and_mark_interruption():

    if not os.path.isfile(LOG_FILE):
        return

    with open(LOG_FILE, "r") as f:
        reader = list(csv.DictReader(f))

        if not reader:
            return

        last_row = reader[-1]

        if last_row.get("mood") not in ["MAINTAIN", "INTERRUPTED"]:

            interrupted_row = {key: "" for key in last_row.keys()}

            interrupted_row["timestamp"] = "SYSTEM INTERRUPTED"
            interrupted_row["mood"] = "INTERRUPTED"

            with open(LOG_FILE, "a", newline="") as wf:
                writer = csv.DictWriter(wf, fieldnames=last_row.keys())
                writer.writerow(interrupted_row)

            add_blank_line()


def log_data(data):

    exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="") as f:

        writer = csv.DictWriter(f, fieldnames=data.keys())

        if not exists:
            writer.writeheader()

        writer.writerow(data)

    if data.get("mood") == "MAINTAIN":
        add_blank_line()