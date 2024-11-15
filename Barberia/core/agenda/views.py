import json

from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView,CreateView,UpdateView, DeleteView

from .forms import AgendaForm
from .models import Agenda

class AgendaListiView(ListView):
    template_name ="Agenda/listaAgendas.html"
    context_object_name = "Agenda"
    model = Agenda
    #queryset = Agenda.objects.filter(usuario=id())

    def get_queryset(self):
        # Filtrar las agendas solo para el usuario autenticado
        return Agenda.objects.filter(usuario=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Listado de Agenda"
        context['query'] = self.request.GET.get("query")
        return context

class AgendaCreateView(CreateView):
    template_name = 'Agenda/agendar_citas.html'
    model = Agenda
    form_class = AgendaForm
    success_url = reverse_lazy('listaagenda')

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['tituloform'] = "Formulario De Agenda"
      context['titulo'] = "Agenda"
      context['boton'] = "Agregar Agenda"
      context['listar_url'] = '/listaagenda/'
      context['action_save'] = '/crearagenda/'
      return context

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Asigna el usuario actual
        return super().form_valid(form)

    # def form_invalid(self, form):
    #     # En caso de errores de validación, devolvemos un JSON con los errores
    #     errors = form.errors.as_json()
    #     print(errors)
    #     return JsonResponse({'errors': json.loads(errors)})


class actualizarAgenda(UpdateView):
  model = Agenda
  template_name = "Agenda/agendar_citas.html"
  success_url = reverse_lazy('listaagenda')
  form_class = AgendaForm

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['action_save'] = self.request.path
    context['title'] = 'Actualización'
    context['tituloform'] = 'ACTUALIZAR AGENDA'
    context['listar_url'] = '/listaagenda/'
    context['boton'] = "Actualizar"
    return context

class eliminarAgenda(DeleteView):
  model = Agenda
  template_name = "Agenda/eliminarAgenda.html"
  success_url = reverse_lazy('listaagenda')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['action_save'] = self.request.path
    context['title'] = 'Eliminar'
    context['listar_url'] = '/listaagenda'
    context['table_title'] = 'Seguro Que Deseas Eliminar este Registro?'
    return context

  def post(self, request, pk, *args, **kwargs):
      # object = Refrigeradora.objects.get(id=pk)
      # object.estado = True
      # object.save()
      return redirect('listaagenda')