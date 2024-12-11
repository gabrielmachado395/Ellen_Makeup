from django import forms

class VendaForm(forms.Form):
    codigo_produto = forms.CharField(label='Código do Produto', max_length=100)
    quantidade = forms.IntegerField(label='Quantidade')