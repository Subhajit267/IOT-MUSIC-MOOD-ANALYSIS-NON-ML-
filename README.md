<div align="center">

# 🎵 IoT Music Mood Analysis

*A Raspberry Pi based physiological mood detection and music therapy system*

<img src="https://img.shields.io/badge/Python-3.7%2B-blue?logo=python">
<img src="https://img.shields.io/badge/Raspberry%20Pi-4B%2B-c51a4a?logo=raspberry-pi">
<img src="https://img.shields.io/badge/Platform-IoT-green">
<img src="https://img.shields.io/badge/Status-Prototype-orange">

</div>

---

# 📖 Overview

**IoT Music Mood Analysis** is an experimental IoT system that monitors physiological signals and determines a user's emotional state.
Based on the detected mood, the system automatically plays **therapeutic music** to stabilize or improve the emotional condition.

The project runs on a **Raspberry Pi** and integrates multiple sensors to measure:

* Heart Rate
* Blood Oxygen (SpO₂)
* Skin Conductance (GSR)
* Motion Stability

These signals are analyzed in real time to estimate mood and trigger a suitable **music therapy response**.

---

# 🧠 System Concept

The system uses physiological signals related to the **autonomic nervous system** to infer emotional states.

Example:

| Signal     | Emotional Indicator           |
| ---------- | ----------------------------- |
| Heart Rate | Arousal / excitement          |
| GSR        | Stress level                  |
| Motion     | Stability / valid measurement |

These values are combined to classify mood states like:

* Calm
* Nervous
* Angry
* Happy

Once detected, **therapy music** is played to guide the user toward a healthier emotional state.

---

# 🏗 Architecture

The system follows a **layered modular architecture**.

```
mood_reboot/
│
├── analysis/              # Signal processing and mood detection
│   ├── heart_rate.py
│   ├── mood_engine.py
│   └── stress_detector.py
│
├── config/                # Thresholds and system parameters
│   └── settings.py
│
├── sensors/               # Hardware interfaces
│   ├── max30102.py
│   ├── gsr.py
│   ├── mpu6050.py
│   └── motion_filter.py
│
├── therapy/               # Music selection and playback
│   └── music_player.py
│
├── runtime/               # Runtime operating modes
│   ├── full_mode.py
│   ├── raw_mode.py
│   └── simulation_mode.py
│
├── utils/                 # Helper utilities
│   ├── display.py
│   ├── helpers.py
│   ├── logger.py
│   ├── log_viewer.py
│   └── system_info.py
│
└── main.py                # Main menu controller
```

---

# ⚙ System Operating Modes

The system provides **three runtime modes**.

## 1️⃣ Full System Mode

Uses real sensors and performs full therapy.

Flow:

```
Sensor Reading
     ↓
Motion Stability Check
     ↓
Heart Rate & SpO2 Calculation
     ↓
Stress Detection
     ↓
Mood Classification
     ↓
Music Therapy Trigger
```

Music plays until the track finishes before the next measurement cycle begins.

---

## 2️⃣ Raw Sensor Debug Mode

Displays **real-time physiological data** every **5 seconds**.

Used for:

* sensor calibration
* debugging
* raw signal monitoring

Music playback is **disabled** in this mode.

---

## 3️⃣ Simulation Mode

Runs the system using **pre-recorded physiological datasets** stored in CSV format.

Used for:

* demonstration
* testing without hardware
* algorithm validation

---

# 🎯 Mood Detection Logic

Mood classification uses a **rule-based decision system**.

| Heart Rate | Stress Level | Mood    |
| ---------- | ------------ | ------- |
| High       | High         | Angry   |
| Elevated   | Medium       | Nervous |
| Low        | Low          | Calm    |
| Otherwise  | —            | Happy   |

The system then maps mood to a **therapy objective**.

| Current Mood | Therapy Goal |
| ------------ | ------------ |
| Angry        | Calm         |
| Nervous      | Calm         |
| Calm         | Happy        |
| Happy        | Maintain     |

---

# 🎧 Music Therapy System

Music tracks are organized into folders based on therapy goals.

```
therapy/
└── playlists/
    ├── calm/
    │   └── calm1.mp3
    │
    ├── happy/
    │   └── happy1.mp3
    │
    └── maintain/
        └── maintain1.mp3
```

Music playback uses the lightweight CLI player:

```
mpg123
```

---

# 📊 Data Logging

All physiological readings are saved into a CSV file.

```
data/logs/mood_log.csv
```

Each entry records:

```
timestamp
heart_rate
spo2
skin_conductance
motion_magnitude
detected_mood
```

This enables later analysis or visualization.

---

# 🔍 Sensor Stability Protection

Before taking a measurement the system checks motion stability using the **MPU6050 accelerometer**.

If motion exceeds a threshold, the system prints:

```
UNSTABLE CONTACT
Movement detected during reading
```

Measurement is skipped until the hand is stable.

---

# 🚀 Installation

## 1️⃣ Clone repository

```
git clone https://github.com/Subhajit267/IOT-MUSIC-MOOD-ANALYSIS.git
cd IOT-MUSIC-MOOD-ANALYSIS/mood_reboot
```

---

## 2️⃣ Install dependencies

```
pip install numpy smbus2 adafruit-circuitpython-ads1x15
```

---

## 3️⃣ Install audio player

```
sudo apt update
sudo apt install mpg123
```

---

## 4️⃣ Enable I2C

```
sudo raspi-config
```

Navigate to:

```
Interface Options → I2C → Enable
```

---

# ▶ Usage

Start the system:

```
python3 main.py
```

Main menu:

```
1 Full system
2 Raw sensor debug
3 Simulation mode
4 View logs
5 System info
6 Exit
```

---

# 🔮 Future Improvements

* Machine learning based mood detection
* Real-time physiological signal graphs
* Web dashboard monitoring
* Mobile app integration
* Cloud data storage
* Wearable form factor

---

# 👤 Author

**Subhajit Halder**

Email
[subhajithalder267@outlook.com](mailto:subhajithalder267@outlook.com)

---

<div align="center">

Built with
🥧 Raspberry Pi
🐍 Python

</div>
