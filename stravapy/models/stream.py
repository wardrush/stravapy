

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
        
    def __repr__(self):
        # There is no reasonable way to represent the data
       return f"{self.__class__.__name__}(original_size={self.original_size}, resolution='{self.resolution}', series_type='{self.series_type}')"


class StreamSet:
    pass


class AltitudeStream(BaseStream):
    """
    An array of data that shows the altitude at each recorded point
    """

    def __init__(self, data=None, *args, **kwargs):
        """
        Look to BaseStream docs for other parameters
        
        :param data: The data recorded at each point
        :type data: list
        """
        super().__init__(*args, **kwargs)
        self.data = data
        
    def __repr__(self):
        return super().__repr__()
        

class CadenceStream(BaseStream):
    """
    An array of data that shows the pedal cadence at each recorded point
    """
    
    def __init__(self, data=None, *args, **kwargs):
        """
        Look to BaseStream docs for other parameters
        
        :param data: The data recorded at each point
        :type data: list
        """
        super().__init__(*args, **kwargs)
        self.data = data
        
    def __repr__(self):
        return super().__repr__()


class DistanceStream(BaseStream):
    def __init__(self, data=None, *args, **kwargs):
        """
        Look to BaseStream docs for other parameters
        
        :param data: The data recorded at each point
        :type data: list
        """
        super().__init__(*args, **kwargs)
        self.data = data
        
    def __repr__(self):
        return super().__repr__()


class HeartrateStream(BaseStream):
    def __init__(self, data=None, *args, **kwargs):
        """
        Look to BaseStream docs for other parameters
        
        :param data: The data recorded at each point
        :type data: list
        """
        super().__init__(*args, **kwargs)
        self.data = data
        
    def __repr__(self):
        return super().__repr__()


class LatLngStream(BaseStream):
    def __init__(self, data=None, *args, **kwargs):
        """
        Look to BaseStream docs for other parameters
        
        :param data: The data recorded at each point
        :type data: list
        """
        super().__init__(*args, **kwargs)
        self.data = data
        
    def __repr__(self):
        return super().__repr__()


class MovingStream(BaseStream):
    def __init__(self, data=None, *args, **kwargs):
        """
        Look to BaseStream docs for other parameters
        
        :param data: The data recorded at each point
        :type data: list
        """
        super().__init__(*args, **kwargs)
        self.data = data
        
    def __repr__(self):
        return super().__repr__()


class PowerStream(BaseStream):
    def __init__(self, data=None, *args, **kwargs):
        """
        Look to BaseStream docs for other parameters
        
        :param data: The data recorded at each point
        :type data: list
        """
        super().__init__(*args, **kwargs)
        self.data = data
        
    def __repr__(self):
        return super().__repr__()


class SmoothGradeStream(BaseStream):
    def __init__(self, data=None, *args, **kwargs):
        """
        Look to BaseStream docs for other parameters
        
        :param data: The data recorded at each point
        :type data: list
        """
        super().__init__(*args, **kwargs)
        self.data = data
        
    def __repr__(self):
        return super().__repr__()


class SmoothVelocityStream(BaseStream):
    def __init__(self, data=None, *args, **kwargs):
        """
        Look to BaseStream docs for other parameters
        
        :param data: The data recorded at each point
        :type data: list
        """
        super().__init__(*args, **kwargs)
        self.data = data
        
    def __repr__(self):
        return super().__repr__()


class TemperatureStream(BaseStream):
    def __init__(self, data=None, *args, **kwargs):
        """
        Look to BaseStream docs for other parameters
        
        :param data: The data recorded at each point
        :type data: list
        """
        super().__init__(*args, **kwargs)
        self.data = data
        
    def __repr__(self):
        return super().__repr__()


class TimeStream(BaseStream):
    def __init__(self, data=None, *args, **kwargs):
        """
        Look to BaseStream docs for other parameters
        
        :param data: The data recorded at each point
        :type data: list
        """
        super().__init__(*args, **kwargs)
        self.data = data
        
    def __repr__(self):
        return super().__repr__()