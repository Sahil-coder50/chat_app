import logging
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException, ValidationError
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)
def custom_exception_handler(exc, context):
    # Call the default DRF exception handler first
    response = exception_handler(exc, context)
    # Log the exception with context
    logger.error(
        f"Exception: {exc.__class__.__name__} - {str(exc)}",
        extra={"request": context["request"], "view": context["view"]}
    )
    if isinstance(exc, ValidationError):
        response.data = {
            "status_code": response.status_code,
            "errors": response.data,  # preserve field errors
            "exception": exc.__class__.__name__,
        }
        return response

    if response is None:
        return Response(
            {
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "error": str(exc),
                "exception": exc.__class__.__name__,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    response.data = {
        "status_code": response.status_code,
        "errors": response.data,
        "exception": exc.__class__.__name__,
        "view": context["view"].__class__.__name__,
        "method": context["request"].method,
        "path": context["request"].path,
    }

    return response
