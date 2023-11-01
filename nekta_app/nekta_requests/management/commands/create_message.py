from django.core.management import BaseCommand
from nekta_requests.models import RequestMessage, Request


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Create message')
        request = Request.objects.first()
        request_message = RequestMessage.objects.get_or_create(
            text='PROVERKAAAA'
        )

        self.stdout.write(self.style.SUCCESS('Message created'))
        request_message.update(request_id=1)
