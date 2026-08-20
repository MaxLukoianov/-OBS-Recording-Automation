import os
import subprocess
import sys
import time


if len(sys.argv) < 2:
    print("Usage: python record_episode.py <duration_in_minutes>")
    sys.exit(1)

try:
    duration_minutes = float(sys.argv[1])
except ValueError:
    print("Please enter a valid number of minutes.")
    sys.exit(1)

record_duration = duration_minutes * 60

# Update this path to match your OBS installation
obs_exe = r"C:\Program Files\obs-studio\bin\64bit\obs64.exe"
obs_dir = os.path.dirname(obs_exe)

print(f"Starting OBS recording for {duration_minutes} minutes...")

obs_process = subprocess.Popen(
    [obs_exe, "--startrecording", "--minimize-to-tray"],
    cwd=obs_dir
)

# Give OBS time to initialize
time.sleep(2)

# Record for the requested duration
time.sleep(record_duration)

# Stop OBS
obs_process.terminate()
obs_process.wait()

print("Done recording.")