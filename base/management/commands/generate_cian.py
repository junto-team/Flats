from django.core.management.base import BaseCommand
from base.converter.cian import get_yrl


class Command(BaseCommand):
    def handle(self, *args, **options):
        get_yrl()
