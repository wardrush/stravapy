# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 13:08:30 2019

@author: wrush049
"""
from models.athlete import MetaAthlete

class PolylineMap:
    pass


class Route:
    pass


class RouteDirection:
    pass


class SummarySegment:
    pass


class DetailedSegment(SummarySegment):
    pass


class SummarySegmentEffort:
    pass


class DetailedSegmentEffort(SummarySegmentEffort):
    pass


class SegmentLeaderboard(SummarySegment):
    pass


class SegmentLeaderboardEntry(SummarySegment, MetaAthlete):
    pass

class ExplorerResponse:
    """
    A specific class used for segment searching results
    Takes attr of class ExplorerSegment
    """

    def __init__(self, segments=None):
        """
        :param segments: The set of segments matching an explorer request:
        :type segments: Instance of ExplorerSegment
        """
        self.segments = segments


class ExplorerSegment:
    """
    A segment and associated information along with the stretch of route
    """

    def __init__(self,
                 segment_id=None,
                 name=None,
                 climb_category=None,
                 climb_category_desc=None,
                 avg_grade=None,
                 start_latlng=None,
                 end_latlng=None,
                 elev_difference=None,
                 distance=None,
                 points=None):
        """
        :param segment_id: Unique idenfier for the segment
        :type segment_id: float
    
        :param name: The name of the segment
        :type name: string
            
        :param climb_category: The category of the climb. 5 is hardest, 0 is not categorized.
        :type climb_category: int
            
        :param climb_category_desc: Description of climb category. If climb_category = 5, 
                                    climb_category_desc = HC, if c_c = 2, c_c_d = 3, etc.
                                    May be of types: [NC, 1, 2, 3, 4, HC]
                                    Follows convention of https://en.wikipedia.org/wiki/Mountains_classification_in_the_Tour_de_France
        :type climb_category_desc: string
            
        :param avg_grade: The segments average grade in percent
        :type avg_grade: float
            
        :param start_latlng: The starting lat and long
        :type start_latlng: Instance of LatLng
            
        :param end_latlng: The ending lat and long
        :type end_latlng: Instance of LatLng
            
        :param elev_difference: Elevation difference between start and end, in meters
        :type elev_difference: float
            
        :param distance: Segment distance in meters
        :type distance: float
            
        :param points: The polyline map of the segment from Google's algorithm.
                        https://developers.google.com/maps/documentation/javascript/examples/polyline-simple
        :type points: string
        """
        self.segment_id = segment_id
        self.name = name
        self.climb_category = climb_category
        self.climb_category_desc = climb_category_desc
        self.avg_grade = avg_grade
        self.start_latlng = start_latlng
        self.end_latlng = end_latlng
        self.elev_difference = elev_difference
        self.distance = distance
        self.points = points

