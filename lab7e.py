#!/usr/bin/env python3
# Author: Pranav Shrestha
# Student ID: 113964225

class Time:
    """Time object with hour, minute, second."""
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Return time as 'HH:MM:SS'."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Return time as 'HH.MM.SS'."""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'