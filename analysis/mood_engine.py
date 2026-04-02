"""
------------------------------------------------------------
Author: Subhajit Halder
Module: Analysis Layer
File: mood_engine.py

About:
Determines emotional state and therapy objective.

Revisions:
- 2026-03-12 Added therapy objective mapping
------------------------------------------------------------
"""

def detect_mood(hr, stress):

    if hr > 105 and stress in ["HIGH","VERY HIGH"]:
        return "ANGRY"

    if hr > 90:
        return "NERVOUS"

    if hr < 80 and stress == "LOW":
        return "CALM"

    return "HAPPY"


def therapy_target(mood):

    if mood == "ANGRY":
        return "CALM"

    if mood == "NERVOUS":
        return "CALM"

    if mood == "CALM":
        return "HAPPY"

    return "MAINTAIN"