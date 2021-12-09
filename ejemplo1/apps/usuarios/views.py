from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

from .models import Usuario

def usuarios(request):
    return render(request, 'usuarios/usuarios.html')

class ListarAdmin(ListView):
    template_name = "usuarios/admin/listar.html"
    model = Usuario
    context_object_name = "usuarios"

    """
    # return de query + filter
    def get_queryset(self):
        # self.request
        return Usuario.objects.filter(id=1)
    """