# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 13:07:38 2019

@author: wrush049
"""

class MetaClub:
    """
    The lowest detail level for a club. Contains id, resource_state, and name
    """
    
    def __init__(self, 
                 club_id=None,
                 name=None,
                 resource_state=1):
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
        return f"MetaClub({self.club_id}, {self.name})"
    
    def __str__(self):
        return f"MetaClub with ID: {self.club_id} and name: {self.name}"

class SummaryClub(MetaClub):
    pass

class DetailedClub(SummaryClub):
    pass