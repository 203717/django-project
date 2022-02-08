from django.urls import re_path 
from loadImage.views import FirstViewList
from loadImage.views import FirstViewDetail

urlpatterns = [
    re_path(r'^list/$',FirstViewList.as_view()),   
    re_path(r'^list/(?P<pk>\d+)$',FirstViewDetail.as_view()),
]