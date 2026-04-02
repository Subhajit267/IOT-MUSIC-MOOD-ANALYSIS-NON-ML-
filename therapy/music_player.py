"""
------------------------------------------------------------
Author: Subhajit Halder
Module: Therapy Layer
File: music_player.py

About:
Handles therapy music selection and playback.

Revisions:
- 2026-03-12 Added song length wait behaviour
------------------------------------------------------------
"""

import os
import random
import subprocess

BASE = "therapy/playlists"

def choose_song(mood):

    folder = os.path.join(BASE, mood.lower())

    if not os.path.isdir(folder):
        return None

    files=[f for f in os.listdir(folder) if f.endswith(".mp3")]

    if not files:
        return None

    return os.path.join(folder,random.choice(files))


def play_song(song):

    if song is None:
        return

    subprocess.run(["mpg123",song])