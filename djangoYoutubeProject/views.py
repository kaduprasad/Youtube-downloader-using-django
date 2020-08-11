from django.shortcuts import render
from .forms import getLinkForm

def homePage(request):
    return render(request, 'home.html')

def download(request):
    if request.method == 'POST':
        link = getLinkForm(request.POST)
        downloadLink = link.cleaned_data['link']
        quality = link.cleaned_data['quality']
        print(downloadLink,quality)

    link = getLinkForm(request.POST)
    return render(request,'Linkform.html',{'Linkform' : link})