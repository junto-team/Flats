from django.core.management.base import BaseCommand
from base.tasks import get_yrl


class Command(BaseCommand):
    def handle(self, *args, **options):
        get_yrl()
