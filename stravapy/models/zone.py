# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 13:14:33 2019

@author: wrush049
"""

class ZoneRange:
    pass


class ZoneRanges:
    pass


class Zones:
    pass

class TimedZoneRange:
    pass

class TimeZoneDistribution:
    pass

class PowerZoneRanges:
    pass


class HeartRateZoneRanges:
    """
    The training heart rate zones for the user. Can be calculated or manually entered
    """

    def __init__(self, custom_zones=None, zones=None):
        """
        :param custom_zones: Whether the athlete has set custom zones
        :type custom_zones: bool
        
        :param zones: A collection of the maxes and mins of heartrate and power zones 
        :type zones: Instance of ZoneRanges
        """
        self.custom_zones = custom_zones
        self.zones = zones
