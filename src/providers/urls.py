from django.urls import path

from .views import ProvidersView

app_name = "providers"

urlpatterns = [
    path('', ProvidersView.as_view(viewName='Providers'), name="providers")
]

handler404 = "errorpages.views.page_not_found_view"