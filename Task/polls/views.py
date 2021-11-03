from django.shortcuts import render
import pytube


def Run(request):
    return render(request, 'Run.html')


def DownloadAudio(request):

    url = request.GET.get('url')
    youtube = pytube.YouTube(url)
    video = youtube.streams.filter(only_audio=True).first()
    video.download()

    return render(request, 'Download.html')


def Download720p(request):

    url = request.GET.get('url')
    youtube = pytube.YouTube(url)
    video = youtube.streams.filter(res="720p").first()
    video.download()

    return render(request, 'Download.html')


def Download360p(request):

    url = request.GET.get('url')
    youtube = pytube.YouTube(url)
    video = youtube.streams.filter(res="360p").first()
    video.download()

    return render(request, 'Download.html')
