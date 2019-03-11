from time import strftime
from datetime import datetime
from pytz import timezone

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import permissions

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def SystemDateList(request):

    if request.method == 'GET':
        # get the local system date
        now_amsterdam = datetime.now(timezone('Europe/Amsterdam'))
        clock = now_amsterdam.strftime("%Y-%m-%dT%H:%M:%S")

        return Response(str(clock))
