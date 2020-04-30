from django.views.generic import TemplateView, ListView, DetailView


class Index(TemplateView):
    template_name = 'core/index.html'
