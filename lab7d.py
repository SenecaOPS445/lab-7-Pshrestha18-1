#!/usr/bin/env python3

# Author: Pranav Shrestha
# Author ID: 113964225

from lab7a import Time  # Import Time class from lab7a.py
from lab7c import time_difference, format_time  # Import necessary functions from lab7c.py

def get_time_input():
    """Prompts the user to input time in HH:MM:SS format and returns a Time object."""
    time_input = input("Enter time (HH:MM:SS): ")
    
    try:
        # Split the input into hour, minute, and second
        hour, minute, second = map(int, time_input.split(":"))
        
        # Create and return a Time object
        return Time(hour, minute, second)
    except ValueError:
        print("Invalid time format. Please enter time in HH:MM:SS format.")
        return None

# Test the user input functionality
if __name__ == "__main__":
    # Get two times from the user
    print("Enter first time:")
    time1 = get_time_input()
    if time1 is None:
        exit(1)  # Exit if input is invalid
    
    print("Enter second time:")
    time2 = get_time_input()
    if time2 is None:
        exit(1)  # Exit if input is invalid
    
    # Calculate the time difference
    time_diff = time_difference(time1, time2)
    
    # Print the result
    print("Time 1:", format_time(time1))
    print("Time 2:", format_time(time2))
    print("Time difference:", format_time(time_diff))
