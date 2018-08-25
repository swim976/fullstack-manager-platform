from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('people/', include('people.urls')),
    path('oauth/', include('oauth.urls')),
]
