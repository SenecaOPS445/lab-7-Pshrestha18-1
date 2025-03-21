#!/usr/bin/env python3

# Author: Pranav Shrestha
# Author ID: 113964225

from lab7a import Time  # Import Time class from lab7a.py

def change_time(t, seconds):
    """Changes the given time (t) by the specified number of seconds."""
    
    # Convert the current time to total seconds since midnight
    total_seconds = t.hour * 3600 + t.minute * 60 + t.second + seconds
    
    # Ensure the seconds don't overflow
    second = total_seconds % 60
    total_minutes = total_seconds // 60
    minute = total_minutes % 60
    hour = (total_minutes // 60) % 24  # Ensure the hour wraps around after 24
    
    # Return a new Time object with the adjusted time
    return Time(hour, minute, second)

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

# Test the change_time function (you can remove or modify this part for your specific needs)
if __name__ == "__main__":
    # Create a Time object
    time1 = Time(9, 50, 0)
    
    # Change the time by adding 1800 seconds (30 minutes)
    new_time = change_time(time1, 1800)
    
    # Print the result
    print("Original time:", format_time(time1))
    print("New time after adding 1800 seconds:", format_time(new_time))
