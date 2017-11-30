from django.core.management.base import BaseCommand, CommandError
from django.apps import apps


class Command(BaseCommand):
    def handle(self, *args, **options):
        app_models = apps.get_app_config('base').get_models()
        for i in app_models:
            if i.objects.all().count() == 0:
                continue
            print('{}: {}'.format(i._meta.verbose_name, i.objects.all().count()))
            for j in i.objects.all()[:1].values():
                for jj in j.items():
                    if len(str(jj[1])) > 200:
                        continue
                    print("\t{}: {}".format(jj[0], jj[1]))
