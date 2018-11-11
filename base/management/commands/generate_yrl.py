from django.core.management.base import BaseCommand
from base.converter import yandex, cian


class Command(BaseCommand):
    def handle(self, *args, **options):
        yandex.get_yrl()
        cian.get_yrl()
