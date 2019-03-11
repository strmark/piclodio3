"""piclodio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns

# Routers provide an easy way of automatically determining the URL conf.
from webapi.views import BackupFileView
from webapi.views import PlayerView
from webapi.views import SoundView
from webapi.views import WebRadioView
from webapi.views import AlarmClockView
from webapi.views import SystemDateView

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include(router.urls)),
    # 
    path('api-auth/', include('rest_framework.urls')),
    # piclodio URLs
    path('webradio/', WebRadioView.WebRadioList),
    path('webradio/<int:pk>', WebRadioView.WebRadioDetail),

    path('alarms/', AlarmClockView.AlarmClockList),
    path('alarms/<int:pk>', AlarmClockView.AlarmClockDetail),

    path('systemdate/', SystemDateView.SystemDateList),
    path('player/', PlayerView.PlayerStatus),

    path('backup/', BackupFileView.BackupFileView),

    path('volume/', SoundView.VolumeManagement),

]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
