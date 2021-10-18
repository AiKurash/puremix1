from django.shortcuts import render
from .models import imggal

# Create your views here.

def PostList(request):
    project_list = Project.objects.all()

    context = {'projects' : project_list,}

    return render(request , 'videoapp/index.html', context)



def imagedisplay(request):
    resultsdisplay=imggal.objects.all()
    return render(request, 'imagegallery/imagegallery.html',{'imggal':resultsdisplay})
