from django.conf.urls import url
from . import views

app_name = "dashboard"
urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"login", views.login),
    url(r"peoples", views.peoples, name="peoples"),
]
