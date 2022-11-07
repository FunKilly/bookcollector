from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from portal.endpoints.routes import router
from portal.utils.error_handling import (handle_base_exception,
                                         handle_request_validation_exception)
from portal.utils.exceptions import PortalBaseException

app = FastAPI()
app.include_router(router)
app.add_exception_handler(PortalBaseException, handle_base_exception)
app.add_exception_handler(RequestValidationError, handle_request_validation_exception)
