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


class ActivityTotals:
    """
    A roll-up of metric pertaining to a set of activities. 
    Values are in seconds and meters
    """

    def __init__(
        self,
        count=None,
        distance=None,
        moving_time=None,
        elapsed_time=None,
        elevation_gain=None,
        achievement_count=None,
    ):
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
        self.count = count
        self.distance = distance
        self.moving_time = moving_time
        self.elapsed_time = elapsed_time
        self.elevation_gain = elevation_gain
        self.achievement_count = achievement_count


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

    def __init__(
        self,
        score=None,
        distribution_buckets=None,
        zone_type=None,
        sensor_based=None,
        points=None,
        custom_zones=None,
        zone_max=None,
    ):
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
        self.score = score
        self.distribution_buckets = distribution_buckets
        self.zone_type = zone_type
        self.sensor_based = sensor_based
        self.points = points
        self.custom_zones = custom_zones
        self.zone_max = zone_max





class Comment:
    """
    A record of the data and content in an activity comment
    """

    def __init__(
        self,
        comment_id=None,
        activity_id=None,
        text=None,
        athlete=None,
        created_at=None,
    ):
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
        self.comment_id = comment_id
        self.activity_id = activity_id
        self.text = text
        self.athlete = athlete
        self.created_at = created_at


class Error:
    """
    The error returned by Strava's API
    """

    def __init__(self, code=None, field=None, resource=None):
        """
        :param code: The code thrown by the error
        :type code: string
            
        :param field: The query field that threw the error
        :type field: string
            
        :param resource: the resource assocaited with the error
        :type resource: string
        """
        self.code = code
        self.field = field
        self.resource = resource


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



class Fault:
    """
    Encapsulates the Errors returned from API
    """

    def __init__(self, errors=None, message=None):
        """
        :param errors: Set of errrs assocaited with fault (if any)
        :type errors: Instance of Error
        
        :param message: Message of the fault
        :type message: string
        """
        self.errors = errors
        self.message = message


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


class Lap:
    """
    If performing an activity where more than one repetition of the same route 
    is traversed, each will be calculated as a separate lap
    """

    def __init__(self,
                 lap_id=None, 
                 activity=None, 
                 athlete=None, 
                 average_cadence=None, 
                 average_speed=None,
                 distance=None, 
                 elapsed_time=None, 
                 start_index=None, 
                 end_index=None, 
                 lap_index=None, 
                 max_speed=None, 
                 moving_time=None, 
                 name=None, 
                 pace_zone=None, 
                 split=None, 
                 start_date=None,
                 start_date_local=None, 
                 total_elevation_gain=None):
        """
        :param lap_id: Unique identifier of lap. Variable name changed from 
                        Strava's id to avoid keyword conflicts
        :type lap_id: float
        
        :param activity: Originally an instance of MetaActivity, but that class 
                            is just the activity id (type float) so this type
                            will accept either float or MetaActivity
        :type activity: float or MetaActivity
        
        :param athlete: Originally an instance of MetaAthlete, but that class 
                            is just the activity id (type float) so this type
                            will accept either float or MetaAthlete
        :type athlete: float or MetaAthlete
        
        :param average_cadence: The lap's average cadence
        :type average_cadence: float
        
        :param average_speed: The lap's average speed
        :type average_speed: float
        
        :param distance: the lap's distance in meters
        :type distance: float
        
        :param elapsed_time: The lap's elapsed time in seconds
        :type elapsed_time: float
        
        :param start_index: The index of the start in the assocaited ActivityStream
        :type start_index: int
        
        :param end_index: The index of the end in the associated ActivityStream
        :type end_index: int
        
        :param lap_index: The index of the lap in the overall activity.
                            (e.g. if its the 3rd lap of 5, 3)
        :type lap_index: int
        
        :param max_speed: Maximum speed in the lap in meters per second
        :type max_speed: float
        
        :param moving_time: The lap's moving time in seconds
        :type moving_time: int #TODO check if this is correct
        
        :param name: The name of the lap
        :type name: string
        
        :param pace_zone: The athlete's pace zone during the lap
        :type pace_zone: int
        
        :param split: #TODO check this
        :type split: int 
        
        :param start_date: The time at which the lap was started
        :type start_date: DateTime
        
        :param start_date_local: Time at which lap was started in local time
        :type start_date_local: DateTime
        
        :param total_elevation_gain: The elevation gain of the lap in meters
        :type total_elevation_gain: float
        """
        self.lap_id = lap_id
        self.activity = activity
        self.athlete = athlete
        self.average_cadence = average_cadence
        self.average_speed = average_speed
        self.distance = distance
        self.elapsed_time = elapsed_time
        self.start_index = start_index
        self.end_index = end_index
        self.lap_index = lap_index
        self.max_speed = max_speed
        self.moving_time = moving_time
        self.name = name
        self.pace_zone = pace_zone
        self.split = split
        self.start_date = start_date
        self.start_date_local = start_date_local
        self.total_elevation_gain = total_elevation_gain




class MetaActivity:
    """
    The lowest detail level for an activity. Contains only the id
    """

    def __init__(self, activity_id=None):
        """
        :param activity_id: Unique identifier. Renamed from Strava's API to
                            avoid keyword collisions.
        :type activity_id: float
        """
        self.activity_id = activity_id

    def __repr__(self):
        return self.activity_id

    def __str__(self):
        return f"MetaActivity with ID: {self.activity_id}"


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
        return self.athlete_id
    
    def __str__(self):
        return f"MetaAthlete with ID: {self.athlete_id}"


class MetaClub:
    """
    The lowest detail level for a club. Contains id, resource_state, and name
    """
    
    def __init__(self, 
                 club_id=None,
                 resource_state=None, 
                 name=None):
        """
        :param club_id: Unique identifier. Renamed from Strava's API to avoid
                        keyword collisions.
        :type club_id: int
        
        :param resource_state: Indicates level of detail. Will always be 1 in
                                Meta classes
        :type resource_state: int
        
        :param name: The club's name
        :type name: string
        """
        self.club_id = club_id
        self.resource_state = resource_state
        self.name = name
        
    def __repr__(self):
        return self.club_id
    
    def __str__(self):
        return f"MetaClub with ID: {self.club_id} and name: {self.name}"


class PhotosSummary_primary:
    """
    Parent class of PhotosSummary
    """
    
    def __init__(self, photos_summary_id=None, source=None, unique_id=None, urls=None):
        """
        :param photos_summary_id:
        :type photos_summary_id:
        
        :param source:
        :type source:
        
        :param unique_id:
        :type unique_id:
        
        :param urls: Static urls for each of the photos posted
        :type urls: string
        """
        self.photos_summary_id = photos_summary_id
        self.source = source
        self.unique_id = unique_id
        self.urls = urls


class PhotosSummary(PhotosSummary_primary):
    """
    Subclass of PhotosSummary_primary. On its own only has # of photos as attr
    """
    def __init__(self, count=None, primary=None):
        """
        :param count: The number of photos
        :type count: int
        
        :param primary: An instance of PhotosSummary_primary
        :type primary: Instance of PhotosSummary_primary
        """
        super()
        self.count = count
        self.primary = primary


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

class BaseStream:
    """
    The parent class for all Streams.
    Describes attributes about Stream such as size, resolution, and type
    """

    def __init__(self, original_size=None, resolution=None, series_type=None):
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
        self.original_size = original_size
        self.resolution = resolution
        self.series_type = series_type


class AltitudeStream(BaseStream):
    """
    An array of data that shows the altitude at each recorded point
    """

    def __init__(self, original_size=None, resolution=None, series_type=None, data=None):
        """

        :param original_size:
        :param resolution:
        :param series_type:
        :param data:
        """
        super().__init__(original_size, resolution, series_type)
    pass


class CadenceStream(BaseStream):
    pass


class DetailedGear:
    pass


class DetailedSegment:
    pass


class DetailedSegmentEffort:
    pass


class DistanceStream(BaseStream):
    pass


class HeartrateStream(BaseStream):
    pass


class LatLngStream(BaseStream):
    pass


class MovingStream(BaseStream):
    pass


class PowerStream(BaseStream):
    pass


class SmoothGradeStream(BaseStream):
    pass


class SmoothVelocityStream(BaseStream):
    pass


class SummaryActivity:
    pass


class SummaryAthlete:
    pass


class SummaryClub:
    pass


class TemperatureStream(BaseStream):
    pass


class TimeStream(BaseStream):
    pass


class TimedZoneRange:
    pass


class DetailedActivty:
    pass


class DetailedAthlete:
    pass


class DetailedClub:
    pass
