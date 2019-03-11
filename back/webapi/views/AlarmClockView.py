from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import permissions

from webapi.utils.CrontabManager import CrontabManager
from webapi.models import AlarmClock
from webapi.serializers.AlarmClockSerializer import AlarmClockSerializer
from webapi.views import Utils

@api_view(['GET','POST'])
@permission_classes((permissions.AllowAny,))
def AlarmClockList(request):

    if request.method == 'GET':
        alarmclocks = AlarmClock.objects.all()
        serializer = AlarmClockSerializer(alarmclocks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AlarmClockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # create a job line
            last_alarmclock = AlarmClock.objects.latest('id')
            Utils.add_job_in_crontab(last_alarmclock)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def AlarmClockDetail(request, pk):
    """
    Retrieve, update or delete a WebRadio instance.
    """
    try:
        alarmclock = AlarmClock.objects.get(pk=pk)
    except AlarmClock.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        serializer = AlarmClockSerializer(alarmclock)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AlarmClockSerializer(alarmclock, data=request.data)
        if serializer.is_valid():
            serializer.save()
            updated_alarmclock = AlarmClock.objects.get(pk=pk)
            # remove the job from the crontab
            job_comment = "piclodio%s" % updated_alarmclock.id
            CrontabManager.remove_job(job_comment)
            # add it back with new info
            Utils.add_job_in_crontab(updated_alarmclock)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # remove the line from the crontab
        job_comment = "piclodio%s" % alarmclock.id
        CrontabManager.remove_job(job_comment)
        # remove from the database
        alarmclock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
