# Generated by Django 5.1.2 on 2024-11-05 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0009_carrinho_itemcarrinho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
