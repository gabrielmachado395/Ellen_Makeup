from .models import Carrinho
class AtualizarCarrinhoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            try:
                carrinho = Carrinho.objects.get(usuario=request.user)
                request.session['cart_count'] = carrinho.quantidade
            except Carrinho.DoesNotExist:
                request.session['cart_count'] = 0
        return self.get_response(request)
        