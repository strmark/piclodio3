import os

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import permissions

from webapi.models import BackupMusic
from webapi.serializers.FilelUploadSerializer import FileUploadSerializer

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def BackupFileView(request):

    if request.method == 'GET':
        backup_file = BackupMusic.objects.all()
        serializer = FileUploadSerializer(backup_file, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FileUploadSerializer(data=request.data)

        if serializer.is_valid():
            # delete the existing MP3 file if exist
            backup_files = BackupMusic.objects.all()
            for el in backup_files:
                os.remove(el.backup_file.path)
                el.delete()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
