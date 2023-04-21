from django.views.generic.base import TemplateView

from .models import Provider

class ProvidersView(TemplateView):
    template_name = "providers/providers.html"
    viewName = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['viewName'] = self.viewName
        context["providers_list"] = Provider.objects.all()
        return context