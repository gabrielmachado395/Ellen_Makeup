import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, ItemCarrinho, Carrinho
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def home(request):
    produtos = Produto.objects.all()  # Busca todos os produtos do banco de dados 
    return render(request, 'home.html', {'produtos':produtos})  # Renderiza os produtos na página inicial

def produto_detalhes(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'produtos_detalhes.html', {'produto': produto})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Loga o usuário automaticamente após o cadastro
            return redirect('home') # Redireciona para a página inicial após o login
        else:
            return render(request, 'registration/signup.html', {'form': form}) # Retorna a página com os erros
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho, created = Carrinho.objects.get_or_create(usuario=request.user)

    item = carrinho.itens.filter(produto=produto).first()
    if item:
        item.quantidade += 1
        item.save()
        messages.success(request, f"A quantidade de {produto.nome} foi atualizada no carrinho")
    else:
        ItemCarrinho.objects.create(carrinho=carrinho, produto=produto, quantidade=1)
        messages.success(request, f"{produto.nome} foi adicionado ao carrinho!")

    # Atualiza o contador na sessão
    request.session['cart_count'] = carrinho.quantidade

    messages.success(request, f'{produto.nome} foi adicionado ao carrinho!')
    return redirect('ver_carrinho')

@login_required
def remover_do_carrinho(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id, carrinho__usuario=request.user)

    # Remova o item
    item.delete()

    # Atualizar o contador de itens no carrinho da sessão
    carrinho = Carrinho.objects.get(usuario=request.user)
    request.session['cart_count'] = ItemCarrinho.objects.filter(carrinho=carrinho).count()

    messages.success(request, f'{item.produto.nome} foi removido do carrinho!')
    return redirect('ver_carrinho')


@login_required
def ver_carrinho(request):
    carrinho = Carrinho.objects.get(usuario=request.user)
    itens = carrinho.itens.all()
    return render(request, 'ver_carrinho.html', {'carrinho': carrinho, 'itens': itens})

@login_required
def finalizar_pedido(request):
    carrinho = Carrinho.objects.get(usuario=request.user)
    itens = ItemCarrinho.objects.filter(carrinho=carrinho)
    total = sum(item.total for item in itens)

    # Dados para enviar ao Lambda
    payload = {
        'usuario': request.user.username,
        'itens': [{'produto': item.produto.nome, 'quantidade': item.quantidade} for item in itens],
        'total': str(total)
    }

    # URL do endopoint do API Gateway
    url_api_gateway = "https://gwwwx6qppa.execute-api.eu-north-1.amazonaws.com/prod/checkout"

    try:
        response = requests.post(url_api_gateway, json=payload)
        resposta = response.json()

        if resposta.get('success'):
            messages.success(request, 'Pedido realizado com sucesso!')
            # Limpe o carrinho após a compra
            itens.delete()
            return redirect('base')
        else:
            messages.error(request, resposta.get('message', 'Erro ao processar o pedido.'))
            return redirect('ver_carrinho')
    except requests.RequestException as e: 
        messages.error(request, f'Erro ao comunicar com o servidor de pagamento: {e}')
        return redirect('ver_carrinho')
    
def atualizar_quantidade(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id, carrinho__usuario=request.user)
    if 'acao' in request.POST:
        if request.POST['acao'] == 'aumentar':
            item.quantidade += 1
        elif request.POST['acao'] == 'diminuir' and item.quantidade > 1:
            item.quantidade -= 1
        item.save()
    return redirect('ver_carrinho')

def remover_item(request, item_id):
    item = Carrinho.objects.get(id=item_id, usuario=request.user)
    item.delete()
    return redirect('ver_carrinho')