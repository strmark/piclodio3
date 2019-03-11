from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import permissions

from webapi.utils.CrontabManager import CrontabManager
from webapi.models import WebRadio, AlarmClock
from webapi.serializers.WebRadioSerializer import WebRadioSerializer

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def WebRadioList(request):

    if request.method == 'GET':
        webradios = WebRadio.objects.all()
        serializer = WebRadioSerializer(webradios, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WebRadioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def WebRadioDetail(request, pk):
    """
    Retrieve, update or delete a WebRadio instance.
    """
    try:
        webradio = WebRadio.objects.get(pk=pk)
    except WebRadio.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        serializer = WebRadioSerializer(webradio)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WebRadioSerializer(webradio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        # when we delete a web radio, all alarm based on this on will be deleted to, remove them from the contab before
        all_alarms_which_use_the_web_radio_to_delete = AlarmClock.objects.filter(webradio=webradio)
        for alarm in all_alarms_which_use_the_web_radio_to_delete:
            # remove the job from the crontab
            job_comment = "piclodio%s" % alarm.id
            CrontabManager.remove_job(job_comment)
        # then we can safely delete the web radio
        webradio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
