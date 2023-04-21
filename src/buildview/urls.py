from django.urls import path

from .views import HomeView, ProjectView
# from django.views.generic.base import RedirectView

app_name = "buildview"

# The url and viewName are decoupled from the view, so we can change it here without
# having to edit view or template code.
# If you change it here though, you will also have to change it in sidebar and sidebar-mobile.
urlpatterns = [
    # path("", RedirectView.as_view(url='home/')),
    path('home/', HomeView.as_view(viewName='Home'), name="home"),
    path('servers/', ProjectView.as_view(slug='servers', viewName='Servers'), name="servers"),
    path('microservice/', ProjectView.as_view(slug='microservice', viewName='Miroservice'), name="microservice"),
    path('clients/', ProjectView.as_view(slug='clients', viewName='Clients'), name="clients"),
    path('product/', ProjectView.as_view(slug='product', viewName='PRODUCT'), name="product"),
    # path('<str:string>/<slug:build_slug>/', BuildDetailView.as_view(), name="builddetail"),
]
