from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView

class indexTemplateView(TemplateView):
  template_name = "inicio/secciones.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['titulo'] = "Inicio"
    return context