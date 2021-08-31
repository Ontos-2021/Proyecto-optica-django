from django.core.management.base import BaseCommand
from usuarios.models import Usuario
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Asigna usuarios a los grupos'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("--- Creando usuarios ---"))

        Usuario.objects.create_superuser(username="root", password="root", email=None)

        secretaria = Usuario.objects.create_user(username="secretaria", password="secretaria")
        Group.objects.get(name="Secretaría").user_set.add(secretaria)

        profesional_medico = Usuario.objects.create_user(username="profesional_medico", password="profesional_medico")
        Group.objects.get(name="Profesional medico").user_set.add(profesional_medico)

        ventas = Usuario.objects.create_user(username="ventas", password="ventas") 
        Group.objects.get(name="Ventas").user_set.add(ventas)

        taller = Usuario.objects.create_user(username="taller", password="taller")
        Group.objects.get(name="Taller").user_set.add(taller)

        gerencia = Usuario.objects.create_user(username="gerencia", password="gerencia")
        Group.objects.get(name="Gerencia").user_set.add(gerencia)

        self.stdout.write(self.style.SUCCESS("--- Usuarios creados ---"))