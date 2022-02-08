from django.urls import re_path 
from loadImage.views import ListaView
from loadImage.views import DetailView

urlpatterns = [
    re_path(r'^lista/$',ListaView.as_view()),   
    re_path(r'^lista/(?P<pk>\d+)$',DetailView.as_view()),
]