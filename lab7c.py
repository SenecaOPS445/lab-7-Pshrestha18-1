#!/usr/bin/env python3

# Author: Pranav Shrestha
# Author ID: 113964225

from lab7a import Time  # Import Time class from lab7a.py

def time_difference(t1, t2):
    """Returns the difference between two time objects (t1 and t2) as a Time object."""
    
    # Convert both times to total seconds since midnight
    total_seconds_t1 = t1.hour * 3600 + t1.minute * 60 + t1.second
    total_seconds_t2 = t2.hour * 3600 + t2.minute * 60 + t2.second
    
    # Calculate the absolute difference in seconds
    diff_seconds = abs(total_seconds_t1 - total_seconds_t2)
    
    # Convert the difference back to hours, minutes, and seconds
    hour = diff_seconds // 3600
    minute = (diff_seconds % 3600) // 60
    second = diff_seconds % 60
    
    # Return a new Time object with the time difference
    return Time(hour, minute, second)

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

# Test the time_difference function (you can remove or modify this part for your specific needs)
if __name__ == "__main__":
    # Create Time objects
    time1 = Time(10, 30, 0)
    time2 = Time(12, 0, 0)
    
    # Calculate the difference
    time_diff = time_difference(time1, time2)
    
    # Print the result
    print("Time 1:", format_time(time1))
    print("Time 2:", format_time(time2))
    print("Time difference:", format_time(time_diff))
