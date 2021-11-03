from django.urls import path
from .views import Run,Download720p,Download360p,DownloadAudio

urlpatterns = [
    path('', Run, name='run'),
    path('downloadaudio/', DownloadAudio),
    path('download720p/',Download720p),
    path('download360p/',Download360p),


]
