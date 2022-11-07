from fastapi import status


class PortalBaseException(Exception):
    """
    Base exception class for the Blueprint. All Blueprint exceptions must subclass this one.
    """

    status_code: status = status.HTTP_400_BAD_REQUEST
    message: str = None
    field: str = None

    def __init__(
        self,
        status_code: status = None,
        message: str = None,
        field: str = None,
    ):
        if status_code:
            self.status_code = status_code
        if message:
            self.message = message
        if field:
            self.field = field

    def __str__(self):
        """Method overridden to keep the attributes' values in Sentry"""
        data = {
            "field": self.field,
            "message": self.message,
            "status_code": self.status_code,
        }
        return str(data)


class BookAlreadyExists(PortalBaseException):
    message = "Book with provided ISBN already exists."
    field = "ISBN"


class BookNotFound(PortalBaseException):
    message = "Book not fouhnd."
