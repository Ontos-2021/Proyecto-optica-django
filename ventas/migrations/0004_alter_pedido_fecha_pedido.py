# Generated by Django 3.2.5 on 2021-08-25 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='fecha_pedido',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
