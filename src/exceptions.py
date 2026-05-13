class DataError(Exception):
    """Base exception for data-related errors."""
    pass


class MissingDataError(DataError):
    """Raised when expected data is missing."""
    pass


class InvalidStageError(DataError):
    """Raised when invalid stage values are found."""
    pass
