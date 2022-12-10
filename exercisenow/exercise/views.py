from django.shortcuts import render
from .models import Video
from .forms import VideoForm

# Create your views here.
# def index(request):

#     context = {

#     }
#     return render(request, 'index.html', context=context)

def index(request):

    lastvideo= Video.objects.last()

    videofile = lastvideo.videofile if lastvideo else None

    form= VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    
    context= {'videofile': videofile,
              'form': form
              }
    
      
    return render(request, 'index.html', context=context)
    