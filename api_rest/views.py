from django.shortcuts import render
from .models import Produto

def pagina_home(request):
    mensagem = ''

    if request.method == 'POST':
        if 'btn_cadastrar' in request.POST:
            nome = request.POST.get('nome')
            codigo = request.POST.get('codigo')
            quantidade = request.POST.get('quantidade')
            preco = request.POST.get('preco')
            if nome and codigo and quantidade and preco:
                Produto.objects.create(
                    nome=nome,
                    codigo=codigo,
                    quantidade=int(quantidade),
                    preco=float(preco)
                )
                mensagem = 'Produto cadastrado com sucesso.'
            else:
                mensagem = 'Preencha todos os campos para cadastrar.'

        elif 'btn_procurar' in request.POST:
            termo = request.POST.get('nome')
            produtos = Produto.objects.filter(nome__icontains=termo) | Produto.objects.filter(codigo__icontains=termo)
            return render(request, 'home.html', {'produtos': produtos, 'mensagem': mensagem})

        elif 'remover_produto' in request.POST:
            codigo = request.POST.get('codigo')
            Produto.objects.filter(codigo=codigo).delete()
            mensagem = f'Produto com código {codigo} removido.'

        elif 'atualizar_quantidade' in request.POST:
            codigo = request.POST.get('codigo')
            nova_quantidade = request.POST.get('nova_quantidade')
            try:
                produto = Produto.objects.get(codigo=codigo)
                produto.quantidade = int(nova_quantidade)
                produto.save()
                mensagem = f'Quantidade do produto {produto.nome} atualizada.'
            except Produto.DoesNotExist:
                mensagem = 'Produto não encontrado.'

    produtos = Produto.objects.all()
    return render(request, 'home.html', {'produtos': produtos, 'mensagem': mensagem})
