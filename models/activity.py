from .strava_models import ActivityTotals

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
    pass


class DetailedActivty(SummaryActivity):
    pass