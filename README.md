# OBS Recording Automation

A Python automation script that starts an OBS Studio recording, records for a user-specified amount of time, and then automatically closes OBS.

## Features

- Start OBS Studio automatically
- Specify recording duration from the command line
- Automatically convert minutes to seconds
- Minimize OBS to the system tray while recording
- Automatically stop OBS after the specified duration
- Basic command-line input validation

## Requirements

- Python 3.x
- OBS Studio
- Windows

## Setup

1. Install [OBS Studio](https://obsproject.com/).

2. Make sure OBS is configured with your desired recording settings.

3. Update the `obs_exe` variable in `record_episode.py` if OBS is installed in a different location:
