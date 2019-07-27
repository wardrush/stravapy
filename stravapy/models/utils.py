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
        return f"LatLng({self.lat}, {self.long})"
    
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
    def __init__(self, count=None, primary=None, *args, **kwargs):
        """
        :param count: The number of photos
        :type count: int
        
        :param primary: An instance of PhotosSummary_primary
        :type primary: Instance of PhotosSummary_primary
        """
        super().__init__(*args, **kwargs)
        self.count = count
        self.primary = primary



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
        
class UpdateableActivity:
    pass


class Upload:
    pass