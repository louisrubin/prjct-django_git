from django.shortcuts import render

from apps.usuarios.models import Usuario

# vista basada en funcion
def home(request):

    usuarios = Usuario.objects.all()    # genera una query del tipo 'SELECT * ' con .all()
    usuario1 = Usuario.objects.get(id=1)

    print(request.POST.get('username', None))
    print(request.POST.get('password', None))

    context = {
        "usuarios": usuarios,
    }

    return render(request, 'index.html', context)
