from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hola$', views.index, name='index'),
]
