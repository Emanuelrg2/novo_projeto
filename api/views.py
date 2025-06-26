from django.shortcuts import render, redirect
from .models import Produto

def pagina_home(request):
    mensagem = ''
    produtos = Produto.objects.all()

    if request.method == 'POST':
        if 'nova_quantidade' in request.POST:
            codigo = request.POST.get('codigo')
            nova_qtd = request.POST.get('nova_quantidade')

            try:
                produto = Produto.objects.get(codigo=codigo)
                produto.quantidade = int(nova_qtd)
                produto.save()
                mensagem = f'Quantidade do produto "{produto.nome}" atualizada para {nova_qtd}.'
            except Produto.DoesNotExist:
                mensagem = 'Produto não encontrado para atualização.'

        elif 'remover_produto' in request.POST:
            codigo = request.POST.get('codigo')
            try:
                produto = Produto.objects.get(codigo=codigo)
                produto.delete()
                mensagem = f'Produto "{produto.nome}" removido com sucesso.'
            except Produto.DoesNotExist:
                mensagem = 'Produto não encontrado para remoção.'

        elif 'btn_cadastrar' in request.POST:
            nome = request.POST.get('nome')
            codigo = request.POST.get('codigo')
            quantidade = request.POST.get('quantidade')
            preco = request.POST.get('preco')

            if Produto.objects.filter(codigo=codigo).exists():
                mensagem = 'Já existe um produto com esse código.'
            else:
                Produto.objects.create(
                    nome=nome,
                    codigo=codigo,
                    quantidade=quantidade,
                    preco=preco
                )
                mensagem = f'Produto "{nome}" cadastrado com sucesso.'

        elif 'btn_procurar' in request.POST:
            termo = request.POST.get('nome')
            produtos = Produto.objects.filter(nome__icontains=termo) | Produto.objects.filter(codigo__icontains=termo)

    return render(request, 'home.html', {
        'produtos': produtos,
        'mensagem': mensagem
    })
