from django.urls import path

from . import views

app_name = 'videoapp'

urlpatterns = [
    path('', views.PostList, name='home'),
    path('about/', views.About, name='about'),
    path('photos/', views.Photos, name='photos'),
    path('<slug:slug>/', views.DetailView, name='DetailView'),
]
