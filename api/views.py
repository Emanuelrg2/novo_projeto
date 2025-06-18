from api.forms import CreateDataForm
from rest_framework.decorators import api_view  # Importando o decorador api_view
from django.shortcuts import redirect, render # Importando render e redirect

@api_view(['POST'])
def CRUD_create(request):
    if request.method == "POST":
        received_form = CreateDataForm(request.POST)
    
    if received_form.is_valid():
        received_form.save()
        return redirect('api_rest:nome')
    else:
        received_form = CreateDataForm() # Adicionado para exibir o formulário GET
        return render(request, 'home.html', {'form': received_form})
