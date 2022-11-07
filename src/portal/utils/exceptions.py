from fastapi import status
from fastapi.exceptions import RequestValidationError


class BaseException(RequestValidationError):
    def __init__(self, message="", errors=None):
        """
        Arguments called in the caller code have precedence over pre-configured messages and codes.
        """
        if message:
            self.message = message
        if errors:
            self.errors = errors
        super().__init__(self.message)


class BookNotFound(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    message = "Book not found."


class BookAlreadyExists(BaseException):
    status_code = status.HTTP_400_BAD_REQUEST
    message = "Book already exists"
