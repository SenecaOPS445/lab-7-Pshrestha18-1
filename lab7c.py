#!/usr/bin/env python3

# Author: Pranav Shrestha
# Author ID: 113964225

from lab7b import *

def time_to_sec(time):
    """Convert a time object to a single integer representing the number of seconds from mid-night."""
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):
    """Convert a given number of seconds to a time object in hour, minute, second format."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time