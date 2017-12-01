from lxml import etree
import datetime as dt
import json

from django.http import HttpResponse
from django.template import loader

from base.models import *

commercial_types = {}
for i in AnysiteObjectspecies.objects.all():
    commercial_types[str(i.id)] = i.name


def button(request):
    template = loader.get_template('button.html')
    return HttpResponse(template.render({}, request))


def get_comm_type(val):
    types = {
        "Земля под коммерческую застройку": "land",
        "Земли промназначения": "land",
        "Земли сельхозназначения": "land",
        "Усадьба": "hotel",
        "Автостоянка ": "auto repair",
        "Гараж": "auto repair",
        "Помещение под производство ": "manufacturing",
        "Автосервис": "auto repair",
        "Автозаправка": "auto repair",
        "Автомойка": "auto repair",
        "ПСН": "free purpose",
        "Офис": "office",
        "ОСЗ": "free purpose",
        "Торговая площадь": "land",
        "Общепит": "public catering",
        "Склад": "warehouse",
        "Дома, Коттеджи, Таунхаусы": "hotel",
        "Гостиничный комплекс ": "hotel",
        "Турбаза": "hotel",
        "Бизнес-центр": "office",
        "Торговый центр": "retail",
        "Продажа бизнеса": "business",
        "Готовый бизнес": "business",
    }
    wrong_types = {
        "Земельные участки под ИЖС": "",
        "Ивестиционный проект": "",
        "Земли сельхозназначения под дачное строительство": "",
        "Квартира": "",

    }

    try:
        return types[val]
    except:
        if val in wrong_types.keys():
            raise Exception('wrong object commercial type')

    return val


def commerc_to_yrl(offer, attrs):
    yrl_category = etree.SubElement(offer, 'category')
    yrl_category.text = 'коммерческая'

    yrl_type = etree.SubElement(offer, 'type')
    yrl_type.text = 'аренда' if 'Аренда' == attrs.get('objectTypeS', 'Аренда') else 'продажа'

    yrl_creation_date = etree.SubElement(offer, 'creation-date')
    yrl_creation_date.text = dt.datetime.now().isoformat()

    yrl_last_update_date = etree.SubElement(offer, 'last-update-date')
    yrl_last_update_date.text = dt.datetime.now().isoformat()

    yrl_floor= etree.SubElement(offer, 'floor')
    yrl_floor.text = attrs.get('objectFloor', 'Аренда')

    # append_location(offer, attrs)
    # append_sales_agent(offer, attrs)
    # append_price(offer, attrs)
    # append_area(offer, attrs)

    for i in attrs.get('object-objectspecies', '').split('||'):
        yrl_commercial_type = etree.SubElement(offer, 'commercial-type')
        yrl_commercial_type.text = get_comm_type(commercial_types[i])

    try:
        images = json.loads(attrs.get('object-images', ''))
        for i in images:
            url = 'http://mezonn.ru/template/images/{}'.format(i['image'])
            yrl_image = etree.SubElement(offer, 'image')
            yrl_image.text = url
    except:
        pass

    if 'Аренда' == attrs.get('objectTypeS', 'Аренда'):
        yrl_deal_status = etree.SubElement(offer, 'deal-status')
        yrl_deal_status.text = 'direct rent'


def yrl(request):
    # Create the root element
    xml = etree.Element('realty-feed', xmlns="http://webmaster.yandex.ru/schemas/feed/realty/2010-06")
    date_element = etree.SubElement(xml, 'generation-date')
    date_element.text = str(dt.datetime.now())
    for i in AnysiteSiteContent.objects.filter(template=10)[:100]:
        attrs = {}
        obj_type = ''
        for j in AnysiteSiteTmplvarContentvalues.objects.filter(contentid=i.id):
            templv = AnysiteSiteTmplvars.objects.filter(id=j.tmplvarid).values('name')[0]
            if templv['name'] == 'objectTypeS':
                obj_type = j.value
                continue
            attrs[templv['name']] = j.value

        if obj_type in ['Загородная недвижимость', 'Квартиры']:
            pass
        elif obj_type == 'Коммерческая недвижимость':
            offer = etree.SubElement(xml, 'offer', internal_id=str(i.id))
            commerc_to_yrl(offer, attrs)

    return HttpResponse(
        etree.tostring(xml, encoding='UTF-8', pretty_print=True),
        content_type="application/xml"
    )
