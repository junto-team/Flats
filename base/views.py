from lxml import etree
import datetime as dt
import json

from django.http import HttpResponse
from django.template import loader
from django.utils.html import escape

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


def get_live_type(val):
    types = {
        "Усадьба": "дом с участком",
        "Дома, Коттеджи, Таунхаусы": "дача",
        "Земельные участки под ИЖС": "участок",
        "Земли сельхозназначения под дачное строительство": "участок",
        "Квартира": "квартира",
    }
    wrong_types = {
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
        "Земля под коммерческую застройку": "land",
        "Земли промназначения": "land",
        "Земли сельхозназначения": "land",
        "Гостиничный комплекс ": "hotel",
        "Турбаза": "hotel",
        "Бизнес-центр": "office",
        "Торговый центр": "retail",
        "Продажа бизнеса": "business",
        "Готовый бизнес": "business",
        "Ивестиционный проект": ""
    }

    try:
        return types[val]
    except:
        if val in wrong_types.keys():
            return None

    return val


def get_repair(value):
    types = {
        'Без ремонта': '',
        'Косметический ремонт': 'частичный ремонт',
        'Капитальный ремонт': 'хороший',
        'Евро-ремонт': 'евро',
    }
    try:
        return types[value]
    except:
        return ''


def get_home_type(value):
    types = {
        'Блочный': 'блочный',
        'Деревянный': 'деревянный',
        'Другое': '',
        'Железобетон': '',
        'Каркасно-щитовой': '',
        'Кирпичный': 'кирпичный',
        'Кирпично-Монолитный': 'кирпично-монолитный',
        'Металоконструкции': '',
        'Монолит': 'монолит',
        'Панельный': 'панельный',
        'Сендвич-панели': '',
        'Сталинский': ''
    }

    try:
        return types[value]
    except:
        return ''


def append_location(offer, attrs):
    yrl_location = etree.SubElement(offer, 'location')

    yrl_country = etree.SubElement(yrl_location, 'country')
    yrl_country.text = 'Россия'

    try:
        region_id = attrs.get('objectRegions', None)
        region = AnysiteRegions.objects.filter(id=region_id)[0].name
        yrl_region = etree.SubElement(yrl_location, 'region')
        yrl_region.text = region
    except:
        pass

    if attrs.get('objectRegionIrr', ''):
        yrl_region_irr = etree.SubElement(yrl_location, 'locality-name')
        yrl_region_irr.text = attrs.get('objectRegionIrr', '')

    address = attrs.get('object-address', '')
    if address:
        yrl_address = etree.SubElement(yrl_location, 'address')
        yrl_address.text = escape(address)
    else:
        street = attrs.get('objectStreet', '')
        home_numb = attrs.get('objectHomeNumber', '')
        if street and home_numb:
            yrl_address = etree.SubElement(yrl_location, 'address')
            yrl_address.text = "{}, {}".format(street, home_numb)


def append_metro(offer, attrs):
    metro_ids = attrs.get('objectMetro', '').split('||')
    time_on_foot = attrs.get('objectDistanceMetro', '')
    if not (attrs.get('objectMetro', '') and time_on_foot):
        return

    for i in AnysiteMetro.objects.filter(id__in=metro_ids):
        yrl_metro = etree.SubElement(offer, 'metro')
        yrl_metro_name = etree.SubElement(yrl_metro, 'name')
        yrl_metro_name.text = i.name
        yrl_foot_time = etree.SubElement(yrl_metro, 'time-on-foot')
        yrl_foot_time.text = time_on_foot


def append_sales_agent(offer, attrs):
    person_id = attrs.get('objectPerson', '')
    if not person_id:
        return

    yrl_agent = etree.SubElement(offer, 'sales-agent')
    try:
        ptitle = AnysiteSiteContent.objects.get(id=person_id).pagetitle
    except:
        ptitle = ''
    yrl_name = etree.SubElement(yrl_agent, 'name')
    yrl_name.text = ptitle

    for i in AnysiteSiteTmplvarContentvalues.objects.filter(contentid=person_id):
        templv = AnysiteSiteTmplvars.objects.get(id=i.tmplvarid)
        if templv.name == 'emailPerson':
            yrl_email = etree.SubElement(yrl_agent, 'email')
            yrl_email.text = i.value
        if templv.name == 'phonePerson':
            yrl_phone = etree.SubElement(yrl_agent, 'phone')
            yrl_phone.text = i.value


    yrl_category = etree.SubElement(yrl_agent, 'category')
    yrl_category.text = 'агентство'

    yrl_organization = etree.SubElement(yrl_agent, 'organization')
    yrl_organization.text = escape('Агентство недвижимости "Мезон&quot"')

    yrl_url = etree.SubElement(yrl_agent, 'url')
    yrl_url.text = 'http://mezonn.ru/'


def append_price(offer, attrs):
    yrl_price = etree.SubElement(offer, 'price')

    value = attrs.get('object_price', '')
    if value:
        yrl_value = etree.SubElement(yrl_price, 'value')
        yrl_value.text = value

    value = attrs.get('objectCurrency', '')
    if value:
        links = {
            'Рубли': 'RUB',
            'Доллары': 'USD',
            'Евро': 'EUR'
        }
        yrl_currency = etree.SubElement(yrl_price, 'currency')
        yrl_currency.text = links[value]

    yrl_unit = etree.SubElement(yrl_price, 'unit')
    yrl_unit.text = 'кв. м'

    value = attrs.get('objectCommission', '')
    if value:
        yrl_commission = etree.SubElement(yrl_price, 'commission')
        yrl_commission.text = value

    value = attrs.get('objectTimeRent', '')
    if value:
        yrl_period = etree.SubElement(yrl_price, 'period')
        yrl_period.text = value


def append_area(offer, attrs):
    yrl_area = etree.SubElement(offer, 'area')

    if attrs.get('object_area', ''):
        yrl_value = etree.SubElement(yrl_area, 'value')
        yrl_value.text = attrs.get('object_area', '')

        yrl_unit = etree.SubElement(yrl_area, 'unit')
        yrl_unit.text = 'кв. м'
    else:
        yrl_value = etree.SubElement(yrl_area, 'value')
        yrl_value.text = attrs.get('objectAreaTerritory', '')

        yrl_unit = etree.SubElement(yrl_area, 'unit')
        yrl_unit.text = 'cотка'


def generate_yrl(offer, attrs):
    yrl_type = etree.SubElement(offer, 'type')
    yrl_type.text = 'аренда' if 'Аренда' == attrs.get('objectTypeS', 'Аренда') else 'продажа'

    yrl_creation_date = etree.SubElement(offer, 'creation-date')
    yrl_creation_date.text = dt.datetime.now().isoformat()

    yrl_last_update_date = etree.SubElement(offer, 'last-update-date')
    yrl_last_update_date.text = dt.datetime.now().isoformat()

    append_location(offer, attrs)
    append_metro(offer, attrs)
    append_sales_agent(offer, attrs)
    append_price(offer, attrs)
    append_area(offer, attrs)

    if attrs.get('objectFloor', ''):
        yrl_floor = etree.SubElement(offer, 'floor')
        yrl_floor.text = attrs.get('objectFloor', '')

    if attrs.get('objectDirection', ''):
        for direct in attrs.get('objectDirection', '').split('||'):
            yrl_direct = etree.SubElement(offer, 'direction')
            yrl_direct.text = direct

    if attrs.get('objectDistanceCity', ''):
        yrl_distance = etree.SubElement(offer, 'distance')
        yrl_distance.text = attrs.get('objectDistanceCity', '')

    if attrs.get('objectCountRoom', ''):
        yrl_distance = etree.SubElement(offer, 'rooms')
        yrl_distance.text = attrs.get('objectCountRoom', '')

    if attrs.get('objectHeightRoof', ''):
        yrl_distance = etree.SubElement(offer, 'ceiling-height')
        yrl_distance.text = attrs.get('objectHeightRoof', '')

    repair = get_repair(attrs.get('objectRepair', ''))
    if repair:
        yrl_distance = etree.SubElement(offer, 'renovation')
        yrl_distance.text = repair

    try:
        images = json.loads(attrs.get('object-images', ''))
        for i in images:
            url = 'http://mezonn.ru/template/images/{}'.format(i['image'])
            yrl_image = etree.SubElement(offer, 'image')
            yrl_image.text = url
    except:
        pass

    if attrs.get('objectFurniture', ''):
        yrl_furniture = etree.SubElement(offer, 'room-furniture')
        yrl_furniture.text = 'да'

    if attrs.get('objectFurniture', ''):
        yrl_water = etree.SubElement(offer, 'water-supply')
        yrl_water.text = 'да'

    if attrs.get('objectFurniture', ''):
        yrl_sewerage = etree.SubElement(offer, 'sewerage-supply')
        yrl_sewerage.text = 'да'

    if attrs.get('objectFurniture', ''):
        yrl_electro = etree.SubElement(offer, 'electricity-supply')
        yrl_electro.text = 'да'

    if attrs.get('objectFurniture', ''):
        yrl_gas = etree.SubElement(offer, 'gas-supply')
        yrl_gas.text = 'да'

    if attrs.get('objectFurniture', ''):
        yrl_gas = etree.SubElement(offer, 'heating-supply')
        yrl_gas.text = 'да'


def add_extra_commercial(offer, attrs):
    yrl_category = etree.SubElement(offer, 'category')
    yrl_category.text = 'коммерческая'

    yrl_deal_status = etree.SubElement(offer, 'deal-status')
    yrl_deal_status.text = 'direct rent'

    if attrs.get('object-objectspecies', ''):
        for i in attrs.get('object-objectspecies', '').split('||'):
            yrl_commercial_type = etree.SubElement(offer, 'commercial-type')
            yrl_commercial_type.text = get_comm_type(commercial_types[i])


def add_extra_living(offer, attrs):
    yrl_deal_status = etree.SubElement(offer, 'property-type')
    yrl_deal_status.text = 'жилая'

    yrl_deal_status = etree.SubElement(offer, 'deal-status')
    yrl_deal_status.text = 'sale'

    yrl_gas = etree.SubElement(offer, 'pool')
    yrl_gas.text = 'да' if attrs.get('objectFurniture', '') == 'yes' else 'нет'

    if attrs.get('objectFloorAll', ''):
        yrl_floors_all= etree.SubElement(offer, 'floors-total')
        yrl_floors_all.text = attrs.get('objectFloorAll', '')

    if attrs.get('objectHomeHousing', ''):
        yrl_floors_all= etree.SubElement(offer, 'building-section')
        yrl_floors_all.text = attrs.get('objectHomeHousing', '')

    if attrs.get('objectFloor', ''):
        yrl_floor = etree.SubElement(offer, 'rooms-offered')
        yrl_floor.text = attrs.get('objectFloor', '')

    home_type = get_home_type(attrs.get('objectFloorAll', ''))
    if home_type:
        yrl_floors_all = etree.SubElement(offer, 'objectHomeType')
        yrl_floors_all.text = home_type

    if attrs.get('object-objectspecies', ''):
        for i in attrs.get('object-objectspecies', '').split('||'):
            cat = get_live_type(commercial_types[i])
            if not cat:
                continue
            yrl_category = etree.SubElement(offer, 'category')
            yrl_category.text = cat
            break


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

        offer = etree.SubElement(xml, 'offer', internal_id=str(i.id))
        generate_yrl(offer, attrs)
        if obj_type in ['Загородная недвижимость', 'Квартиры']:
            add_extra_living(offer, attrs)
        elif obj_type == 'Коммерческая недвижимость':
            add_extra_commercial(offer, attrs)

    return HttpResponse(
        etree.tostring(xml, encoding='UTF-8', pretty_print=True),
        content_type="application/xml"
    )
