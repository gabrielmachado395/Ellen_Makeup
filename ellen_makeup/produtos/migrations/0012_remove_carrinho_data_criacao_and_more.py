# Generated by Django 5.1.2 on 2024-11-21 13:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0011_remove_produto_code_delete_venda'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrinho',
            name='data_criacao',
        ),
        migrations.RemoveField(
            model_name='itemcarrinho',
            name='preço',
        ),
        migrations.AlterField(
            model_name='itemcarrinho',
            name='carrinho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='produtos.carrinho'),
        ),
        migrations.AlterField(
            model_name='itemcarrinho',
            name='quantidade',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
