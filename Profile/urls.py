from Profile.views import RegisterIdView
from django.urls import path, re_path

urlpatterns = [    
    re_path(r'^v1/profile/(?P<pk>\d+)$', RegisterIdView.as_view())
]