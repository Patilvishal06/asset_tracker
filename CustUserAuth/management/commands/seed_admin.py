from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Seed the admin user'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(is_superuser=True).exists():
            admin = User.objects.create_superuser(
                email='admin@neosoft.com',
                password='1234',
                username='admin'
            )
            system_admin_group, _ = Group.objects.get_or_create(name='SystemAdmin')
            admin.groups.add(system_admin_group)

            self.stdout.write(self.style.SUCCESS('Admin user seeded successfully.'))
        else:
            self.stdout.write(self.style.WARNING('Admin user already exists.'))
