#!/usr/bin/env python3

# Author: Pranav Shrestha
# Stdent ID: 113964225

class Time:
    """Time object with hour, minute, second."""
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        """Overload the + operator to add two Time objects."""
        total_seconds = self.time_to_sec() + other.time_to_sec()
        return self.sec_to_time(total_seconds)

    def time_to_sec(self):
        """Convert time to total seconds."""
        return self.hour * 3600 + self.minute * 60 + self.second

    @staticmethod
    def sec_to_time(seconds):
        """Convert total seconds to Time object."""
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return Time(hours, minutes, seconds)

    def __str__(self):
        """Return time as 'HH:MM:SS'."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
