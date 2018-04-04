from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^yrl$', views.manual_yrl, name='manual_yrl'),
    url(r'^r87klfvse72yl0lx6m8k$', views.yrl, name='yrl'),
    url(r'^r87klfafy72yl0lx6m8k$', views.yrl_afy, name='yrl'),
    url(r'^r87kflats72yl0lx6m8k$', views.yrl_flats, name='yrl'),
    url(r'^r87kdom72yl0lx6m8k$', views.yrl_domklick, name='yrl'),  #dom cklick
]