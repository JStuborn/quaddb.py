# errors.py

class QuadDBError(Exception):
    """Base class for all QuadDB API exceptions."""
    pass

class InvalidParameterError(QuadDBError):
    """Raised when a parameter is invalid."""
    pass

class NotFoundError(QuadDBError):
    """Raised when a resource is not found."""
    pass

class ServerError(QuadDBError):
    """Raised when the server encounters an error."""
    pass
