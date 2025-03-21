#!/usr/bin/env python3

# Author: Pranav Shrestha
# Author ID: 113964225

from lab7a import Time  # Import Time class from lab7a.py
from lab7c import time_difference, format_time  # Import necessary functions from lab7c.py
from lab7e import valid_time  # Import valid_time function from lab7e.py

# Test all the functionalities
if __name__ == "__main__":
    # Create Time objects for testing
    time1 = Time(10, 30, 0)
    time2 = Time(12, 0, 0)
    time3 = Time(23, 59, 59)  # Edge case time
    
    # Check time difference
    time_diff = time_difference(time1, time2)
    
    # Validate times
    print("Time 1 valid:", valid_time(time1))
    print("Time 2 valid:", valid_time(time2))
    print("Time 3 valid:", valid_time(time3))
    
    # Print time difference
    print("Time difference between Time 1 and Time 2:", format_time(time_diff))
