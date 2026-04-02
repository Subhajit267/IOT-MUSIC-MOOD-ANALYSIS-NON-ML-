"""
------------------------------------------------------------
Author: Subhajit Halder
Date Created: 2026-03-12
Module: Configuration
File: settings.py

About:
Stores threshold values and configuration parameters
used across the entire system.

Revisions:
- 2026-03-12 Initial implementation
------------------------------------------------------------
"""

# ------------------------------------------------------------
# Heart rate thresholds (beats per minute)
# ------------------------------------------------------------

HR_HIGH = 110     # high physiological arousal
HR_MEDIUM = 90    # moderate heart rate


# ------------------------------------------------------------
# GSR thresholds (raw ADC values)
# ------------------------------------------------------------

GSR_HIGH = 20000
GSR_MEDIUM = 16000


# ------------------------------------------------------------
# Motion detection threshold
# ------------------------------------------------------------

MOTION_THRESHOLD = 20000


# ------------------------------------------------------------
# Retry delay when measurement fails
# ------------------------------------------------------------

RETRY_DELAY = 3