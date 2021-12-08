from django.shortcuts import render

from apps.usuarios.models import Usuario

# vista basada en funcion
def inicio(request):

    context = {
        "usuarios": Usuario.objects.all(),  # genera una query del tipo 'SELECT * ' con .all()   ||||   # usuario1 = Usuario.objects.get(id=1)
    }
    return render(request, 'index.html', context)

def login(request):
    return render(request, 'login.html')
