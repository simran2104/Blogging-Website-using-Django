from . import views
from django.urls import path

# Add URLConf
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.upload, name='upload'),
    
]