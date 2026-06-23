from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet

class BaseAPIView(GenericViewSet):
    """
    Standard API response format
    """

    def success_response(self, data=None, message="Success", status=status.HTTP_200_OK):
        return Response({
            "status": "success",
            "message": message,
            "data": data
        }, status=status)

    def error_response(self, message="Error", status=400):
        return Response({
            "status": "error",
            "message": message,
            "data": None
        }, status=status)