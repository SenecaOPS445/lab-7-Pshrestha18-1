#!/usr/bin/env python3

# Author: Pranav Shrestha
# Author ID: 113964225

from lab7a import Time  # Import Time class from lab7a.py

def valid_time(t):
    """Check the validity of the time object attributes."""
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

# Test the valid_time function
if __name__ == "__main__":
    # Create Time objects for testing
    time1 = Time(10, 30, 0)
    time2 = Time(25, 60, 0)  # Invalid time
    
    # Check validity of times
    print("Time 1 valid:", valid_time(time1))
    print("Time 2 valid:", valid_time(time2))
