#!/usr/bin/env python3

# Author: Pranav Shrestha
# Author ID: 113964225

from lab7a import *

def change_time(time, seconds):
    """Modify the time object by adding seconds."""
    time.second += seconds

    # Handle negative seconds
    while time.second < 0:
        time.second += 60
        time.minute -= 1

    while time.minute < 0:
        time.minute += 60
        time.hour -= 1

    # Handle overflow
    while time.second >= 60:
        time.second -= 60
        time.minute += 1

    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1

    return None