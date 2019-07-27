# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 08:58:47 2019

@author: wrush049
"""
from oauth2_utils import OAuth2Client


class SegmentEfforts:
    """
    Activity segment effort. Strava records data in both streams and segments
    """

    def __init__(self, segment_id=None):
        self.segment_id = segment_id

    def list_segment_efforts(self):
        pass

    def get_segment_effort(self):
        pass


class Segment:
    """
    Activity segment
    """

    def __init__(self, segment_id=None, **kwargs):
        self.segment_id = segment_id

        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_segment_leaderboard(self):
        """
        Returns the specified segment leaderboard
        
        :param id: (Required) Segment id
        :type id: float
        
        :param gender: Filter by gender. Takes 'M' or 'F'
        :type gender: string
        
        :param age_group: [Summmit] Filter by age group. Takes one of following values:
                            [0_19, 20_24, 25_34, 35_44, 45_54, 55_64, 65_74, 75_plus]
        :type age_group: string
        
        :param weight_class: [Summit] Filter by weight class (lb or kg). Takes one of following values:
                            lbs [0_124, 125_149, 150_164, 165_179, 180_199, 200_224, 225_249, 250_plus]
                            kgs [0_54, 55_64, 65_74, 75_84, 85_94, 95_104, 105_114, 115_plus]
        :type weight_class: string
        
        :param following: Filter by friends of authenticated athlete
        :type following: bool
        
        :param club_id: Filter by club
        :type club_id: float
        
        :param date_range: Filter by date range. Takes one of following values:
                            [this_year, this_month, this_week, today]
        :type date_range: string
        
        :param context_entries: TODO not sure what this does. Listed in API docs though
        :type context_entries: int
        
        :param page: Page number if navigating through multipage results
        :type page: int
        
        :param per_page: Number of items to page. Defaults to 30
        :type per_page: int
        """


class Activity(Segment):
    """
    The activity(workout) object. 
    Each activity can be examined as a summary or through the streams.
    """

    def __init__(self):
        pass

    def list_activity_comments(self):
        pass

    def list_activity_laps(self):
        pass

    def get_activity_zones(self):
        pass


class Club:
    """
    Club object
    Describes the club activities, members, admins, etc
    """

    def __init__(
        self, club_id=None, activities=None, administrators=None, members=None, **kwargs
    ):
        self.club_id = club_id
        self.activities = activities if activities is not None else []
        self.administrators = administrators if administrators is not None else []
        self.members = members if members is not None else []

        for key, value in kwargs.items():
            setattr(self, key, value)

    # TODO figure out how best to inialize the club


class Route:
    """
    Route object that contains GPX or TCX directions
    Downloads the file from Strava in preferred format
    """

    def __init__(self, save_format="gpx", save_location=None):
        if save_location is None:
            # TODO Find way to save file in appropriate directory
            pass

    def get_route(self):
        pass


class Athlete(OAuth2Client):
    """
    The user class for the authenticated athlete
    """

    def __init__(self, athlete_id=None, firstname=None, lastname=None, **kwargs):
        """
        Initialize the athlete. Intended to mirror the structure of the dict
        returned by Strava when the user is authenticated.
        
        **kwargs is intended to be extensible for the scope under which the 
        client is viewed. (i.e. if the scope is 'profile:read_all', then the 
        object will have many more attributes than 'profile:read')
        
        More detail can be found in the Strava docs at
        https://developers.strava.com/docs/reference/#api-Athletes-getLoggedInAthlete
        """
        self.athlete_id = athlete_id
        self.firstname = firstname
        self.lastname = lastname

        # TODO could super().__init__(**kwargs) be appropriate here?
        # Set remaining attrs with **kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_authenticated_athlete(self, **kwargs):
        """
        Set attributes for returned athlete. Tokens with profile:read_all scope
        will receive a detailed athlete representation; all others will receive
        a summary representation
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    #################
    # These functions are options pulled from API docs. To be included
    #################
    def create_activity(self):
        pass

    def get_activity(self):
        pass

    def list_athlete_activities(self):
        pass

    def get_zones(self):
        pass

    def get_athlete_stats(self):
        pass

    def update_athlete(self):
        pass

    def list_athlete_clubs(self):
        pass

    def get_equipment(self):
        pass

    def list_athlete_routes(self):
        pass

    def get_running_race(self):
        pass

    def list_running_races(self):
        pass

    def explore_segments(self):
        """
        Explore the top 10 segments matching a query
        
        :param bounds: (Required) Lat/Long for 2 points specifying two corners of a rectangle bounding the segment
        :type bounds: array[floats]
        
        :param activity_type: Filter by activity type (e.g. 'running' or 'riding')
        :type activity_type: string
        
        :param min_cat: Minimum climing category (an integer describing climb difficulty)
        :type min_cat: int
        
        :param max_cat: Maximum climbing category
        :type max_cat: int
        """
