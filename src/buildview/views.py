from django.views.generic.base import TemplateView

from .models import Project, BuildData

class HomeView(TemplateView):
    template_name = 'buildview/home.html'
    viewName = ''

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['viewName'] = self.viewName
        context['projects'] = Project.objects.all()
        context['activity'] = BuildData.objects.all()
        return context

class ProjectView(TemplateView):
    template_name = 'buildview/builds.html'
    slug = ''
    viewName = ''

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['viewName'] = self.viewName
        # Get all the build data and filter by the project slug
        context['object_list'] = BuildData.objects.all().filter(project_slug=self.slug)
        return context
