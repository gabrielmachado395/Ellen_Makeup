# Generated by Django 5.1.2 on 2024-10-20 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0005_venda_quantidade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='cod_produto',
            new_name='code',
        ),
    ]