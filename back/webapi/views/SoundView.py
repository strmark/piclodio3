from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import permissions

from webapi.utils.SoundManager import SoundManager
from webapi.serializers.SoundManagerSerializer import SoundManagerSerializer

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def VolumeManagement(request):

    if request.method == 'GET':
        """
        Get the volume status
        """
        content = {'volume': SoundManager.get_volume()}
        return Response(content)

    elif request.method == 'POST':
        serializer = SoundManagerSerializer(data=request.data)

        if serializer.is_valid():
            SoundManager.set_volume(serializer.validated_data["volume"])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
