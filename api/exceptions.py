from rest_framework.views import exception_handler
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import status


class BadRequestException(Exception):
    def __init__(self):
        super().__init__("Bad Request")


def custom_exception_handler(exc, context):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    response_data = {'error': str(exc)}

    if isinstance(exc, ObjectDoesNotExist):
        status_code = status.HTTP_404_NOT_FOUND
    elif isinstance(exc, BadRequestException):
        status_code = status.HTTP_400_BAD_REQUEST
    elif isinstance(exc, AuthenticationFailed):
        status_code = status.HTTP_401_UNAUTHORIZED

    return Response(response_data, status=status_code)
