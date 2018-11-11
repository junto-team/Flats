import json

from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from base.models import *

class Command(BaseCommand):
    def show_templates(self):
        for i in AnysiteSiteTemplates.objects.all():
            print(i.id, i.templatename)

    def show_tmplvars(self, templ_id):
        for i in AnysiteSiteTmplvarTemplates.objects.filter(templateid=templ_id):
            vars = AnysiteSiteTmplvars.objects.filter(id=i.tmplvarid)
            for v in vars:
                print(v.id, v.name)

    def show_types(self, templ_id):
        types = {}
        val_types = []
        for i in AnysiteSiteContent.objects.filter(template=templ_id)[:10]:
            name = ''
            attrs = []
            for j in AnysiteSiteTmplvarContentvalues.objects.filter(contentid=i.id):
                templv = AnysiteSiteTmplvars.objects.get(id=j.tmplvarid)
                if templv.name == 'objectTypeS':
                    name = j.value
                elif templv.name not in attrs:
                    attrs.append(templv.name + ': ' + templv.type)

                if templv.type not in val_types:
                    val_types.append(templv.type)

            if name not in types.keys():
                types[name] = attrs
        for type, names in types.items():
            print(type)
            for n in names:
                print("\t{}".format(n))
        print("\n", val_types)

    def show_content(self, templ_id):
        types = {}
        for i in AnysiteSiteContent.objects.using('mezon').filter(published=1)[:10]:
            for j in AnysiteSiteTmplvarContentvalues.objects.using('mezon').filter(contentid=i.id):
                #if not j.value or len(j.value) > 100:
                #    continue
                print("\t{}".format(j.value))
                templv = AnysiteSiteTmplvars.objects.using('mezon').get(id=j.tmplvarid)
                #if 'image' in templv.name:
                #    print("\t{}, {}, {}, {}".format(templv.name, templv.type, j.value, json.loads(j.value)[0]['image']))
                for attr, value in templv.__dict__.items():
                    if len(str(value)) > 1000:
                        continue
                    print("\t\t{}: {}".format(attr, value))

    def show_stat(self):
        print('id name amount')
        stat = []
        for t in AnysiteSiteTemplates.objects.all().order_by('id'):
            amount = AnysiteSiteContent.objects.filter(template=t.id).count()
            stat.append((t.id, t.templatename, amount))
        stat.sort(key=lambda x: x[2])
        for s in reversed(stat):
            print(s[0], s[1], s[2])

    def handle(self, *args, **options):
        #for i in AnysiteObjectspecies.objects.all():
        #    print('"{}": "",'.format(i.name))
        #self.show_tmplvars(10)
        #self.show_content(10)
        #self.show_stat()
        self.show_types(10)
