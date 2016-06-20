from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hello$', views.hello),
    url(r'^$', views.index, name='index'),
    url(r'login', views.login),
]
