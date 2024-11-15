from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class registroView(View):
    def get(self,request):
        form = UserCreationForm()
        return render(request, "registro/registrar.html",{"form":form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('iniSesion')
        return render(request, "registro/registrar.html", {"form": form})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registrar'
        return context

