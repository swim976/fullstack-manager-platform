from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dashboard/", include("dashboard.urls", namespace="dashboard")),
    path("people/", include("people.urls", namespace="people")),
    path("oauth/", include("oauth.urls", namespace="oauth")),
]
