from django.urls import path
from . import views
from .views import imagedisplay

app_name = 'imagegallery'

urlpatterns = [
    path('', views.PostList, name='home'),
    path('imagegallery/imagegallery', views.imagedisplay, name='imagegallery'),
    ]
