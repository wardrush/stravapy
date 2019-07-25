# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 13:55:11 2019

@author: wrush049
"""


############
# Create blank classes that mirror Strava's listed classes. Will do inheritance as appropriate
############


class ActivityStats:
    """
    Set of stats and totals for an athlete
    Subclassed by Athlete
    """
    
    def __init__(self, 
                 biggest_ride_distance=None, 
                 biggest_climb_elevation_gain=None, 
                 recent_ride_totals=None, 
                 recent_run_totals=None, 
                 recent_swim_totals=None, 
                 ytd_ride_totals=None, 
                 ytd_run_totals=None, 
                 ytd_swim_totals=None, 
                 all_ride_totals=None, 
                 all_swim_totals=None):
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
            
        :param all_swim_totals:
        :type all_swim_totals:
        
        """

        pass


class ActivityTotals:
    """
    A roll-up of metric pertaining to a set of activities. 
    Values are in seconds and meters
    """
    
    def __init__(self, 
                 count=None,
                distance=None,
                moving_time=None,
                elapsed_time=None,
                elevation_gain=None,
                achievement_count=None):
        """
        Instatiates an ActivityTotals object
    
        :param count:
        :type count:
            
        :param distance:
        :type distance:
            
        :param moving_time:
        :type moving_time:
            
        :param elapsed_time:
        :type elapsed_time:
            
        :param elevation_gain:
        :type elevation_gain:
            
        :param achievement_count:
        :type achievement_count:
        """


        pass

# TODO decide if this should just be made as an attr in activity class
class ActivityTypes:
    """
    An enumeration of the types an activity may have.

    May be one of the following values: 
    [AlpineSki, BackcountrySki, Canoeing, Crossfit, EBikeRide, Elliptical,
    Golf, Handcycle, Hike, IceSkate, InlineSkate, Kayaking, Kitesurf,
    NordicSki, Ride, RockClimbing, RollerSki, Rowing, Run, Sail, Skateboard,
    Snowboard, Snowshoe, Soccer, StairStepper, StandUpPaddling, Surfing, Swim,
    Velomobile, VirtualRide, VirtualRun, Walk, WeightTraining, Wheelchair,
    Windsurf, Workout, Yoga]
    """

    pass


class ActivityZone:
    """
    A description of the heartrate or power zone distributions for an activity
    """
    
    def __init__(self, 
                 score=None, 
                 distribution_buckets=None, 
                 zone_type=None, 
                 sensor_based=None, 
                 points=None, 
                 custom_zones=None, 
                 zone_max=None):
        """
        
        :param score: #TODO not sure what this score is
        :type score: int
            
        :param distribution_buckets: A description of the time spent in each zone
        :type distribution_buckets: Instance of TimedZoneDistribution
            
        :param zone_type: Description of the zone category. May be of types: [heartrate, power]
                            Variable name has been changed from Strava's 'type' to avoid keywords
        :type zone_type: string
            
        :param sensor_based: Recording if the zone data is sensor-based or estimated
        :type sensor_based: bool
            
        :param points: #TODO not sure
        :type points: int
            
        :param custom_zones: Recording if the zones are set by the user manually
        :type custom_zones: bool
            
        :param zone_max: #TODO I think this is an int representing the max zone reached in activity
        :type zone_max: int
        """
        pass
    

class BaseStream:
    """
    The parent class for Streams.
    Describes attributes about Stream such as size, resolution, and type
    """
    
    def __init__(self, 
                 original_size=None, 
                 resolution=None, 
                 series_type=None):
        """
        :param original_size: The number of data points in the stream
        :type original_size: int
            
        :param resolution: Level of detail (sampling) for the stream. 
                            May be of types: [low, medium, high]
        :type resolution: string
            
        :param series_type: Base series used in case stream was downsampled.
                            May be of type: [distance, time]
        :type series_type: string
        """
        pass


class Comment:
    """
    A record of the data and content in an activity comment
    """
    
    def __init__(self, 
                 comment_id=None,
                 activity_id=None,
                 text=None,
                 athlete=None,
                 created_at=None):
        """
        :param comment_id: Unique identifier for comment. Variable name changed
                            from Strava's id to avoid keyword conflicts
        :type comment_id: float
            
        :param activity_id: The activity identifier on which the comment is posted
        :type activity_id: float
            
        :param text: The content of the comment
        :type text: string
            
        :param athlete: #TODO I think the athlete that posted the comment
        :type athlete: Instance of SummaryAthlete
            
        :param created_at: The time at which comment was created. Using format ISO 8601
        :type created_at: DateTime
        """
        pass


class Error:
    """
    The error returned by Strava's API
    """
    
    def __init__(self, 
                 code=None, 
                 field=None, 
                 resource=None):
        """
        :param code: The code thrown by the error
        :type code: string
            
        :param field: The query field that threw the error
        :type field: string
            
        :param resource: the resource assocaited with the error
        :type resource: string
        """
        pass


class ExplorerResponse:
    """
    A specific class used for segment searching results
    Takes attr of class ExplorerSegment
    """
    
    def __init__(self, 
                 segments=None):
        """
        :param segments: The set of segments matching an explorer request:
        :type segments: Instance of ExplorerSegment
        """
        pass


class ExplorerSegment:
    """
    A segment and associated information along with the stretch of route
    """
    
    def __init__(self):
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

        pass


class Fault:
    """
    Encapsulates the Errors returned from API
    """
    
    def __init__(self, 
                 errors=None, 
                 message=None):
        """
        :param errors: Set of errrs assocaited with fault (if any)
        :type errors: Instance of Error
        
        :param message: Message of the fault
        :type message: string
        """
        pass


class HeartRateZoneRanges:
    """
    The training heart rate zones for the user. Can be calculated or manually entered
    """
    
    def __init__(self, 
                 custom_zones=None, 
                 zones=None):
        """
        :param custom_zones: Whether the athlete has set custom zones
        :type custom_zones: bool
        
        :param zones: A collection of the maxes and mins of heartrate and power zones 
        :type zones: Instance of ZoneRanges
        """
        pass
    

class Lap:
    """
    If performing an activity where more than one repetition of the same route 
    is traversed, each will be calculated as a separate lap
    """
    
    def __init__(self,
                 ):
        """
        :param lap_id: Unique identifier of lap. Variable name changed from 
                        Strava's id to avoid keyword conflicts
        :type lap_id: float
        
        :param activity: 
        :type activity:
        
        :param athlete:
        :type athlete:
        
        :param average_cadence:
        :type average_cadence:
        
        :param average_speed:
        :type average_speed:
        
        :param distance:
        :type distance:
        
        :param elapsed_time:
        :type elapsed_time:
        
        :param start_index:
        :type start_index:
        
        :param end_index:
        :type end_index:
        
        :param lap_index:
        :type lap_index:
        
        :param max_speed:
        :type max_speed:
        
        :param moving_time:
        :type moving_time:
        
        :param name:
        :type name:
        
        :param pace_zone:
        :type pace_zone:
        
        :param split:
        :type split:
        
        :param start_date:
        :type start_date:
        
        :param start_date_local:
        :type start_date_local:
        
        :param total_elevation_gain:
        :type total_elevation_gain:
        """
    pass


class LatLng:
    pass


class MetaActivity:
    pass


class MetaAthlete:
    pass


class MetaClub:
    pass


class PhotosSummary:
    pass


class PhotosSummary_primary:
    pass


class PolylineMap:
    pass


class PowerZoneRanges:
    pass


class Route:
    pass


class RouteDirection:
    pass


class RunningRace:
    pass


class SegmentLeaderboard:
    pass


class SegmentLeaderboardEntry:
    pass


class Split:
    pass


class StreamSet:
    pass


class SummaryGear:
    pass


class SummarySegment:
    pass


class SummarySegmentEffort:
    pass


class TimeZoneDistribution:
    pass


class UpdateableActivity:
    pass


class Upload:
    pass


class ZoneRange:
    pass


class ZoneRanges:
    pass


class Zones:
    pass


############
# Stream models
###########


class AltitudeStream:
    pass


class CadenceStream:
    pass


class DetailedGear:
    pass


class DetailedSegment:
    pass


class DetailedSegmentEffort:
    pass


class DistanceStream:
    pass


class HeartrateStream:
    pass


class LatLngStream:
    pass


class MovingStream:
    pass


class PowerStream:
    pass


class SmoothGradeStream:
    pass


class SmoothVelocityStream:
    pass


class SummaryActivity:
    pass


class SummaryAthlete:
    pass


class SummaryClub:
    pass


class TemperatureStream:
    pass


class TimeStream:
    pass


class TimedZoneRange:
    pass


class DetailedActivty:
    pass


class DetailedAthlete:
    pass


class DetailedClub:
    pass
