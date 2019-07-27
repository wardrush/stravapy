class Split:
    pass

class Lap(Split):
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
        return f"MetaActivity({self.activity_id})"

    def __str__(self):
        return f"MetaActivity with ID: {self.activity_id}"

class SummaryActivity(MetaActivity, ActivityTotals):
    #TODO See if info can be copy-pasted from ActivityTotals
    def __init__(self):
        pass


class DetailedActivty(SummaryActivity):
    pass

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
        
class RunningRace:
    pass