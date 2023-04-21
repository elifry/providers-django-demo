from django.urls import path

from .views import NotificationsView
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = "settings"
urlpatterns = [
    path("", RedirectView.as_view(url='notifications/')),
    path('notifications/', NotificationsView.as_view(), name="notifications"), # path('notifications/', TemplateView.as_view(template_name='settings/notifications.html'), name="notifications"),
    path('appearance/', TemplateView.as_view(template_name='settings/appearance.html'), name="appearance"),
    path('connections/', TemplateView.as_view(template_name='settings/connections.html'), name="connections"),
]
