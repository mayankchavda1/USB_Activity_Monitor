# USB Activity Monitor

A lightweight Python-based USB Activity Monitoring and Forensic Logging System designed for endpoint security analysis, suspicious USB behavior detection, and real-time event monitoring.

---

# Features

## USB Monitoring

- Detect USB insertion/removal
- Capture drive information
- Monitor active removable devices

## File Activity Tracking

- Detect file creation events
- Detect executable files
- Monitor suspicious activity

## Logging System

- TXT logs
- CSV forensic logs
- Timestamped security events

## Risk Detection

- Suspicious executable detection
- Risk scoring engine
- Threat level generation

## Real-Time Monitoring

- Continuous USB event monitoring
- Console-based live alerts

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main language |
| psutil | USB detection |
| watchdog | File monitoring |
| colorama | Colored terminal output |
| csv | Log export |
| logging | Event logging |

---

# Project Structure

```text
usb_activity_monitor/
│
├── main.py
├── monitor.py
├── logger.py
├── file_tracker.py
├── risk_engine.py
├── config.py
├── trusted_devices.json
├── requirements.txt
│
├── logs/
│   ├── activity_log.txt
│   ├── activity_log.csv
│   └── alerts.json
│
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/usb-activity-monitor.git
```

## Open Project

```bash
cd usb-activity-monitor
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Project

```bash
python main.py
```

---

# Example Output

```text
==================================================
USB ACTIVITY MONITOR STARTED
==================================================

USB_INSERTED | E:\ | FAT32

FILE_CREATED | E:\resume.pdf

EXECUTABLE_DETECTED | E:\payload.exe

USB_REMOVED | E:\ | Session Duration: 42s
```

---

# Future Improvements

- GUI Dashboard
- Streamlit Web Panel
- Desktop Notifications
- Device Whitelisting
- SHA256 File Hashing
- Process Monitoring
- PowerShell Detection
- Threat Intelligence Engine
- AI-Based Behavior Analysis

---

# Learning Outcomes

This project demonstrates:

- Python automation
- System monitoring
- File handling
- Logging systems
- Basic endpoint security concepts
- Behavioral monitoring
- Cybersecurity project development

---

# Disclaimer

This project is created for educational and research purposes only.

---

# Author

Mayank Chavda

GitHub: https://github.com/mayankchavda1
