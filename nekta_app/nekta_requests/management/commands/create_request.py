from django.contrib.auth.models import User
from django.core.management import BaseCommand
from nekta_requests.models import Request


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Create request')
        user = User.objects.get(username='admin')
        request = Request.objects.get_or_create(
            title='Some request 1',
            description='Test request for my task'
        )

        self.stdout.write(self.style.SUCCESS('Request created'))




