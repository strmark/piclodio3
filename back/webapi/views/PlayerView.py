from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import permissions

from webapi.utils.PlayerManager import PlayerManager
from webapi.models import WebRadio
from webapi.serializers.PlayerSerializer import PlayerManagerSerializer

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def PlayerStatus(request):

    if request.method == 'GET':
        """
        Get the Mplayer status
        """
        if PlayerManager.is_started():
            status = "on"
        else:
            status = "off"

        answer = {
            "status": status
        }
        return Response(answer)

    elif request.method == 'POST':
        serializer = PlayerManagerSerializer(data=request.data)

        if serializer.is_valid():
            new_status = serializer.validated_data["status"]
            if new_status == "on":
                # give a web radio to play is optional
                if "webradio" in serializer.validated_data:
                    webradio = serializer.validated_data["webradio"]
                    url_to_play = webradio.url
                    # remove the is_default from other web radio
                    qs = WebRadio.objects.filter(is_default=True)
                    qs.update(is_default=False)
                    # the selected web radio become the default one
                    webradio.is_default = True
                    webradio.save()

                else:
                    # get the default web radio if exist
                    try:
                        default_web_radio = WebRadio.objects.get(is_default=True)
                        url_to_play = default_web_radio.url
                    except WebRadio.DoesNotExist:
                        # No default web radio
                        answer = {
                            "status": "error, no default web radio"
                        }
                        return Response(answer, status=status.HTTP_400_BAD_REQUEST)

                PlayerManager.play(url_to_play)
                returned_status = "on"
            else:
                PlayerManager.stop()
                returned_status = "off"

            answer = {
                "status": returned_status
            }
            return Response(answer)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
