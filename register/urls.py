from django.urls import path, re_path
from django.conf.urls import include


from register.views import RegisterView

urlpatterns = [
    re_path(r'^', RegisterView.as_view()),    
]