# -*- coding: utf-8 -*-
"""
Utility functions to convert back and forth between a timestring and timedelta.
"""

from django.conf import settings

from datetime import timedelta
import re

ALLOW_MONTHS = getattr(settings, "DURATIONFIELD_ALLOW_MONTHS", False)
ALLOW_YEARS = getattr(settings, "DURATIONFIELD_ALLOW_YEARS", False)
MONTHS_TO_DAYS = getattr(settings, "DURATIONFIELD_MONTHS_TO_DAYS", 30)
YEARS_TO_DAYS = getattr(settings, "DURATIONFIELD_YEARS_TO_DAYS", 365)

def str_to_timedelta(td_str):
    """
    Returns a timedelta parsed from the native string output of a timedelta.

    Timedelta displays in the format ``X day(s), H:MM:SS.ffffff``
    Both the days section and the microseconds section are optional and ``days``
    is singular in cases where there is only one day.

    Additionally will handle user input in months and years, translating those
    bits into a count of days which is 'close enough'.
    """
    if not td_str:
        return None

    # set default values.
    days = 0
    hours = 0
    minutes = 0
    seconds = 0
    microseconds = 0

    split_up = td_str.split(':')
    nbr_fields = len(split_up)

    if nbr_fields == 0: # should never happen
        pass
    if nbr_fields == 1:
        seconds = int(split_up[0])
    elif nbr_fields == 2:
        minutes = int(split_up[0])
        seconds = int(split_up[1])
    elif nbr_fields == 3:
        hours = int(split_up[0])
        minutes = int(split_up[1])
        seconds = int(split_up[2])
    else: # in case there's more than 3 fields ...
        hours = int(split_up[-3])
        minutes = int(split_up[-2])
        seconds = int(split_up[-1])


    return timedelta(
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds,
        microseconds=microseconds)
