"""
------------------------------------------------------------
Author: Subhajit Halder
Module: Utility Layer
File: helpers.py

About:
Provides small helper functions used across
multiple modules in the system.

------------------------------------------------------------
"""

from datetime import datetime


def get_timestamp():

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")