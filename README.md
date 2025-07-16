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

##  Images

| CAD Model | Circuit | Output |
|-----------|---------|--------|
| ![cad](images/cad_render.png) | ![circuit](images/breadboard_photo.jpg) | ![serial](images/serial_output.png) |

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
