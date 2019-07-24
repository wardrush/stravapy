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
    Subclasses by Athlete
    """

    pass


class ActivityTotals:
    """
    A roll-up of metric pertaining to a set of activities. 
    Values are in seconds and meters
    """

    pass


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
    pass


class BaseStream:
    pass


class Comment:
    pass


class Error:
    pass


class ExplorerResponse:
    pass


class ExplorerSegment:
    pass


class Fault:
    pass


class HeartRateZoneRanges:
    pass


class Lap:
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
