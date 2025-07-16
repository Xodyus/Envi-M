# Envi-M


A full-stack Arduino + Python project that tracks environmental conditions to calculate how ideal your surroundings are for focusing and productivity.

## Features

-  Reads **temperature**, **humidity**, and **light intensity**
-  Sends sensor data over Serial to a **Python script**
-  Logs data to **CSV** for tracking trends
-  Calculates a custom **Focus Score** based on thresholds
-  Custom-designed **FreeCAD housing** for neat presentation

##  Tech Stack

- Arduino Uno + DHT11 + Photoresistor
- Python (Serial + CSV logging)
- FreeCAD for 3D housing
- GitHub + Notion for documentation

##  Focus Score Logic

The Python script penalizes the score if:
- Temperature is outside 21–25 °C
- Humidity is outside 40–60%
- Light is too high (>700) for screen work

Final score is capped at 100 and logged with timestamps.
Ideal Score should be ~50

##  Images

# CAD Model
<img width="604" height="328" alt="cad_render png" src="https://github.com/user-attachments/assets/76b686bc-504b-4019-8160-595a073501c5" />

# Circuit
<img width="1139" height="452" alt="breadboard_photo jpg" src="https://github.com/user-attachments/assets/bc55bc5d-93a9-4d14-b0a9-97bf4a689b77" />

##  Files

- `/arduino/environmental_monitor.ino`
- `/python/log_environment.py`
- `/enclosure/monitor_housing.FCStd` (FreeCAD source)
- `/enclosure/monitor_housing.stl` (3D printable)

##  Future Features

- Live dashboard with graphs
- SD card data logging
- RGB LED indicator

---
