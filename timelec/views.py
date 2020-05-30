from django.shortcuts import render
from .models import Video
from .forms import VideoForm


def index(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            videofile = Video.objects.filter().order_by('-id')[0]
            return render(request, './studentvt/index.html', {
                'form': VideoForm(),
                'video': videofile

            })
    else:
        form = VideoForm()
        return render(request, './studentvt/index.html', {
            'form': form
        })
