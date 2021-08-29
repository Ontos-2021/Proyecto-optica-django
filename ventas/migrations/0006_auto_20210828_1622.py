# Generated by Django 3.2.5 on 2021-08-28 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0005_auto_20210828_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('Lentes', 'Lentes'), ('Otros', 'Otros'), ('<django.db.models.fields.related.ManyToManyField>', 'Tipo')], max_length=50),
        ),
        migrations.DeleteModel(
            name='Lente',
        ),
    ]