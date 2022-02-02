from django.urls import re_path 
from primerComponente.views import PrimerViewList
from primerComponente.views import PrimerViewDetail


#importando vistas
from primerComponente.views import PrimerViewList

urlpatterns = [
    re_path(r'^lista/$', PrimerViewList.as_view()),
    re_path(r'^lista/(?P<pk>\d+)$',PrimerViewDetail.as_view()),
]