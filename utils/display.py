"""
------------------------------------------------------------
Author: Subhajit Halder
Module: Utility Layer
File: display.py

About:
Displays monitoring UI and sensor messages.
------------------------------------------------------------
"""

def show_unstable(timestamp):

    print("\n====================================================")
    print("           IoT MOOD REBOOT - MONITOR")
    print("====================================================")

    print("\nTimestamp :", timestamp)

    print("\n---------------- SENSOR STATUS --------------------\n")

    print("Measurement Status     : UNSTABLE CONTACT")
    print("Reason                 : Movement detected during reading\n")
    print("Action                 : Please keep hand steady")

    print("\n====================================================")


def show_monitor(d):

    print("\n====================================================")
    print("           IoT MOOD REBOOT - MONITOR")
    print("====================================================")

    print("\nTimestamp :", d["timestamp"])

    print("\n---------------- RAW SENSOR DATA ------------------\n")

    print("MAX30102 IR Signal      :", d["ir"])
    print("MAX30102 RED Signal     :", d["red"])
    print("GSR Voltage             :", d["gsr_voltage"], "V")
    print("Accelerometer Magnitude :", d["motion"])

    print("\n---------------- PHYSIOLOGICAL DATA ---------------\n")

    print("Heart Rate              :", d["hr"], "BPM")
    print("Blood Oxygen            :", d["spo2"], "%")
    print("Skin Conductance        :", d["gsr"])
    print("Motion Stability        :", d["motion_state"])

    print("\n---------------- ANALYSIS RESULT ------------------\n")

    print("Stress Level            :", d["stress"])
    print("Detected Mood           :", d["mood"])

    print("\n---------------- THERAPY OBJECTIVE ----------------\n")

    print("Current Mood            :", d["mood"])
    print("Target Mood             :", d["target"])

    print("\n---------------- THERAPY MODULE -------------------\n")

    print("Music Triggered         :", d["music"])

    print("\n====================================================")