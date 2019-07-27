# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 11:02:02 2019

@author: wrush049
"""


class MetaAthlete:
    """
    The lowest detail level for an athlete. Contains only the id
    """

    def __init__(self, athlete_id=None):
        """
        :param athlete_id: Unique identifier. Renamed from Strava's API to 
                            avoid keyword collisions.
        :type athlete_id: float
        """
        self.athlete_id = athlete_id
        
    def __repr__(self):
        return f"MetaAthlete({self.athlete_id})"
    
    def __str__(self):
        return f"MetaAthlete with ID: {self.athlete_id}"


class SummaryAthlete(MetaAthlete, ActivityStats):
    pass


class DetailedAthlete(SummaryAthlete):
    pass


class ActivityStats:
    """
    Set of stats and totals for an athlete
    Subclassed by Athlete
    """

    def __init__(
        self,
        biggest_ride_distance=None,
        biggest_climb_elevation_gain=None,
        recent_ride_totals=None,
        recent_run_totals=None,
        recent_swim_totals=None,
        ytd_ride_totals=None,
        ytd_run_totals=None,
        ytd_swim_totals=None,
        all_ride_totals=None,
        all_run_totals=None,
        all_swim_totals=None,
    ):
        """
        Instantiate an ActivityStats object
        
        :param biggest_ride_distance: The longest distance ridden by athlete
        :type biggest_ride_distance: float
        
        :param biggest_climb_elevation_gain: The largest climb ridden by athlete
        :type biggest_climb_elevation_gain: float
        
        :param recent_ride_totals:
        :type recent_ride_totals:
            
        :param recent_run_totals:
        :type recent_run_totals:
            
        :param recent_swim_totals:
        :type recent_swim_totals:
            
        :param ytd_ride_totals:
        :type ytd_ride_totals:
            
        :param ytd_run_totals:
        :type ytd_run_totals:
            
        :param ytd_swim_totals:
        :type ytd_swim_totals:
            
        :param all_ride_totals:
        :type all_ride_totals:

        :param all_run_totals:
        :type all_run_totals:
            
        :param all_swim_totals:
        :type all_swim_totals:
        
        """
        self.biggest_ride_distance = biggest_ride_distance
        self.biggest_climb_elevation_gain = biggest_climb_elevation_gain
        self.recent_ride_totals = recent_ride_totals
        self.recent_run_totals = recent_run_totals
        self.recent_swim_totals = recent_swim_totals
        self.ytd_ride_totals = ytd_ride_totals
        self.ytd_run_totals = ytd_run_totals
        self.ytd_swim_totals = ytd_swim_totals
        self.all_ride_totals = all_ride_totals
        self.all_run_totals = all_run_totals
        self.all_swim_totals = all_swim_totals