from django.shortcuts import render
from .models import Project
from django.views import generic
# Create your views here.

def PostList(request):
    project_list = Project.objects.all()

    context = {'projects' : project_list,}

    return render(request , 'videoapp/index.html', context)

def DetailView(request, slug):
    project_detail = Project.objects.get(slug=slug)

    context = {'project_detail' : project_detail,}

    return render(request , 'videoapp/single_project.html', context)


#class PostList(generic.ListView):
  #ueryset = Project.objects.filter(status=1).order_by('-created_on')
  #template_name = 'videoapp/index.html'


#class DetailView(generic.DetailView):
  #model = Project
  #template_name = 'videoapp/single_project.html'


#def project(request, id, slug):
    #project = Project.objects.get(id=id)
    #context = {
        #'project': project,
    #}
    #return render(request, 'videoapp/single_project.html', context)

def About(request):
    return render(request, 'videoapp/about.html')

def Photos(request):
    return render(request, 'videoapp/blog.html')




#def Contact(request):
    #return render(request, 'videoapp/contact.html')
