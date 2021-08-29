# Generated by Django 3.2.5 on 2021-08-29 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pacientes', '0003_auto_20210828_1823'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(null=True)),
                ('asistencia', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('paciente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pacientes.paciente')),
            ],
            options={
                'verbose_name': 'Turno',
                'verbose_name_plural': 'Turnos',
            },
        ),
    ]