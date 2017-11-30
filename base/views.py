from lxml import etree
import datetime as dt

from django.http import HttpResponse
from django.template import loader

from base.models import *


def button(request):
    template = loader.get_template('button.html')
    return HttpResponse(template.render({}, request))


def yrl(request):
    # Create the root element
    xml = etree.Element('realty-feed', xmlns="http://webmaster.yandex.ru/schemas/feed/realty/2010-06")
    date_element = etree.SubElement(xml, 'generation-date')
    date_element.text = str(dt.datetime.now())
    for i in AnysiteSiteContent.objects.filter(template=10)[:50]:
        print(i.id)
        attrs = {}
        for j in AnysiteSiteTmplvarContentvalues.objects.filter(contentid=i.id):
            if not j.value or len(j.value) > 100:
                continue
            templv = AnysiteSiteTmplvars.objects.get(id=j.tmplvarid)
            attrs[templv.name] = j.value
        offer = etree.SubElement(xml, 'offer', internal_id=str(i.id))
        for name, val in attrs.items():
            param = etree.SubElement(offer, name)
            param.text = val

    return HttpResponse(
        etree.tostring(xml, encoding='UTF-8', pretty_print=True),
        content_type="application/xml"
    )
