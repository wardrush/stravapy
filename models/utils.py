class LatLng:
    """
    A collection of latitude and logitude coordinates (floats)
    """

    def __init__(self,
                 lat=None,
                 long=None):
        """
        Initialize the object's coordinates
        """
        self.lat = lat
        self.long = long

    def __repr__(self):
        """
        Create the representation of this class when called.
        When asked to return, will be returned as [lat, long]
        """
        return [self.lat, self.long]