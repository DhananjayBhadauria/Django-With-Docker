from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import PermissionDenied, NotFound, APIException


class CoreHome(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        # raise APIException('this is my new custome exception here.')
        return Response(data={'details':'Docker Compose worked!'}, status=200)