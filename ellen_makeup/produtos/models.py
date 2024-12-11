from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preço = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) 
    descrição = models.CharField(max_length=200)
    quantidade = models.IntegerField()
    imagem = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return self.nome
        
class Carrinho(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"Carrinho de {self.usuario.username}"

    @property
    def total(self):
        """
        Calcula o subtotal do carrinho somando os totais de todos os itens.
        """
        return sum(item.total for item in self.itens.all())

    @property
    def quantidade(self):
        """
        Calcula a quantidade total de produtos no carrinho.
        """
        return sum(item.quantidade for item in self.itens.all())

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade} * {self.produto.nome} no carrinho de {self.carrinho.usuario.username}"

    @property
    def total(self):
        """
        Calcula o preço total deste item com base na quantidade.
        """
        return self.quantidade * self.produto.preço
