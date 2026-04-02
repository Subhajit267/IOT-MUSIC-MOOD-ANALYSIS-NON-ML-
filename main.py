"""
------------------------------------------------------------
Author: Subhajit Halder
Module: System Core
File: main.py

About:
Main menu controller.

Revisions:
- 2026-03-12 Added sensor safety check
------------------------------------------------------------
"""

import sys

from utils.system_info import system_info, sensors_available
from utils.log_viewer import view_logs


def menu():

    print("\n================================")
    print(" IoT Music Mood Analysis System ")
    print("================================")

    print("1 Full system")
    print("2 Raw sensor debug")
    print("3 Simulation mode")
    print("4 View logs")
    print("5 System info")
    print("6 Exit")


def main():

    while True:

        menu()

        c = input("Select option: ")

        if c == "1":

            if not sensors_available():
                print("\nSensors missing. Full mode disabled\n")
                continue

            from runtime.full_mode import run
            run()

        elif c == "2":

            if not sensors_available():
                print("\nSensors missing. Raw mode disabled\n")
                continue

            from runtime.raw_mode import run
            run()

        elif c == "3":

            from runtime.simulation_mode import run
            run()

        elif c == "4":

            view_logs()

        elif c == "5":

            system_info()

        elif c == "6":

            sys.exit()

        else:

            print("Invalid option")


if __name__ == "__main__":
    main()