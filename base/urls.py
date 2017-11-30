from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.button, name='index'),
    url(r'^load$', views.yrl, name='yrl'),
]