from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Crea los grupos de usuarios'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("--- Creando grupos ---"))
        grupo_secretaria = Group.objects.get_or_create(name="Secretaría")
        grupo_medico = Group.objects.get_or_create(name="Profesional medico")
        grupo_ventas = Group.objects.get_or_create(name="Ventas")
        grupo_taller = Group.objects.get_or_create(name="Taller")
        grupo_gerencia = Group.objects.get_or_create(name="Gerencia")

        self.stdout.write(self.style.SUCCESS("--- Creando permisos ---"))
        

        self.stdout.write(self.style.SUCCESS("--- Asignando permisos ---"))

        self.stdout.write(self.style.SUCCESS("--- Grupos creados y permisos asignados ---"))