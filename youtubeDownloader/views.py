from django.shortcuts import render
from djangoYoutubeProject.forms import getLinkForm
from pytube import YouTube

def youtubeDownload(request):
    if request.method == 'POST':
        formLink = getLinkForm(request.POST)
        if formLink.is_valid():
            downloadLink = formLink.cleaned_data.get('Paste_Video_link')
            print(downloadLink)
            startDownloadingVideo(downloadLink)

    context = {}
    context['linkForm'] = getLinkForm() # set context_id = linkForm

    return render(request, "linkForm.html", context)
    # return render(request,'linkForm.html',{'linkForm' : formLink})


def startDownloadingVideo(youtubeDownloadLink):
    link = str(youtubeDownloadLink)
    SAVE_PATH = "D:/youtubeDownloader/"
    yt = YouTube(link)

    video = selectedVideoQuality(yt)
    video.download(SAVE_PATH)
    print('Task Completed!')


def selectedVideoQuality(yt):
    video = yt.streams.get_by_itag('18')  # 360p

    # video = yt.streams.get_by_itag('135')  # 480p
    #
    # video = yt.streams.get_by_itag('22')  # 720p
    #
    # video = yt.streams.get_by_itag('137')  # 1080p
    return video