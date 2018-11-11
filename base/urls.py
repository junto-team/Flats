from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^yrl$', views.manual_yrl, name='manual_yrl'),
    url(r'^r87klfvse72yl0lx6m8k$', views.yrl),
    url(r'^r87klfafy72yl0lx6m8k$', views.yrl_afy),
    url(r'^r87kflats72yl0lx6m8k$', views.yrl_flats),
    url(r'^r87kdom72yl0lx6m8k$', views.yrl_domklick),  #dom cklick
    url(r'^r87kcian72yl0lx6m8k$', views.feed_cian),  #dom cklick
]