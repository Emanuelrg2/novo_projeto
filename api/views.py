# Imports necessários para a API REST
from requests import Response
from rest_framework import viewsets # Importando viewsets do Django REST Framework
from django.shortcuts import render, redirect # Importando render e redirect do Django
from .forms import CreateDataForm # Importando o formulário CreateDataForm


# Importando o serializer e o modelo necessários
from .serializers import UsuariosSerializer
from .models import Usuarios


# arquivos de viwes para renderisação dos templates

# def form_cadastro_view(request):
#     return render(request, 'cadastro.html')

def consulta_view(request):
    return render(request, 'consulta.html')

# arquivos de views para API REST
class UsuariosViewSet(viewsets.ModelViewSet): 
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    model = Usuarios
    tamplet_name = 'consulta.html'
    context_object_name = 'usuarios'

#arquivos de views para API REST
def cadastro_view(request):
    """
    Esta view lida com a exibição do formulário de cadastro (GET)
    e com o processamento da submissão do formulário (POST).
    """
    if request.method == "POST":
        form = CreateDataForm(request.POST) # Instancia o formulário com os dados POST
        if form.is_valid():
            form.save() # Salva os dados no banco de dados
            return redirect('api:consulta') # Redireciona para a página de consulta
        else:
            # Se a validação falhar, renderiza o template COM O FORMULÁRIO QUE CONTÉM OS ERROS
            return render(request, 'cadastro.html', {'form': form})
    else: # Requisição GET: exibe o formulário vazio
        form = CreateDataForm()
    return render(request, 'cadastro.html', {'form': form})

def consulta_view(request):
    """
    Esta view busca todos os itens da tabela Usuarios e os renderiza
    em um template HTML.
    """
    # 1. Obter todos os objetos (itens) do modelo Usuarios
    #    O .objects é o "manager" do modelo, e .all() retorna um QuerySet de todos os objetos.
    todos_usuarios = Usuarios.objects.all()

    # 2. Passar os objetos para o template no contexto
    context = {
        'usuarios': todos_usuarios # O nome 'usuarios' será usado no template para iterar sobre eles
    }

    # 3. Renderizar o template 'consulta.html' com os dados
    return render(request, 'consulta.html', context)
