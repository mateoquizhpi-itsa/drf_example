import os

import django
from django.contrib.auth.models import User, Group, Permission
from django.core.management import BaseCommand

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('++++++++++++++++++++++++ INGRESANDO DATA BASE DEL PROYECTO ++++++++++++++++++++++++ ')
        print("++++++++++++++++++++++++ CREANDO USUARIO ADMINISTRADOR ++++++++++++++++++++++++")
        user_admin = User.objects.create(
            username='admin',
            first_name='Admin',
            is_active=True,
            is_superuser=True,
            is_staff=True
        )
        user_admin.set_password('1st44dm1n2024*+')
        user_admin.save()
        print(f'Bienvenido {user_admin.first_name} {user_admin.last_name}')
