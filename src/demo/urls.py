from django.urls import path
from demo.views import list_slides, list_layouts
from django.views.generic import TemplateView

app_name = "demo"
urlpatterns = [
    path('slides/', list_slides, name="slides"),
    path('what-is-devops/', TemplateView.as_view(template_name='demo/slides/devops.html'), name="devops"),
    path('layouts/', list_layouts, name="layouts"),
    path('dashboard-react-tailwind/', TemplateView.as_view(template_name='demo/layouts/dashboard_react_tailwind.html'), name="dashboard-react-tailwind"),
    path('dashboard-plain-tailwind/', TemplateView.as_view(template_name='demo/layouts/dashboard_plain_tailwind.html'), name="dashboard-plain-tailwind"),
    path('settings-tailwind/', TemplateView.as_view(template_name='demo/layouts/settings_tailwind.html'), name="settings-tailwind"),
]
