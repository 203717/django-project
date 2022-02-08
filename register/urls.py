from django.urls import re_path

from register.views import RegistroView

urlpatterns = [
    re_path(r'^', RegistroView.as_view()),    
]