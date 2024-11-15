from django.contrib.auth.views import LoginView,LogoutView
from django.shortcuts import redirect


class inicioSesionUsuario(LoginView):
    template_name = 'iniciarSesion/iniciosesion.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Iniciar sesión'
        return context