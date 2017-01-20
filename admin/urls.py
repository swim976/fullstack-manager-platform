from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/', include('dashboard.urls', namespace='dashboard')),
    url(r'^people/', include('people.urls', namespace='people')),
    url(r'^oauth/', include('oauth.urls', namespace='oauth')),
]
