from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('settings/', include('settings.urls')),
    path('buildadmin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('providers/', include('providers.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]

handler404 = "errorpages.views.page_not_found_view"
