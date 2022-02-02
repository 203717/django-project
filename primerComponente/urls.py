from django.urls import re_path 

#importando vistas
from primerComponente.views import PrimerViewList

urlpatterns = [
    re_path(r'^lista/$', PrimerViewList.as_view()),
   
]