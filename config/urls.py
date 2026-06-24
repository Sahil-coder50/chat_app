from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path("admin/", admin.site.urls),
    # HealthCheck
    path("health/", lambda request: HttpResponse("ok")),

    # APP
    path("api/v1/", include("modules.chats.urls")),
]