from lxml import etree
import datetime as dt
import json
import re
import urllib.request

from django.utils.html import escape
from django.utils import timezone

from base.models import *
from base.converter.helpers import download_data
from base.converter import keys


def get_exchange_rate(currency='USD'):
    try:
        contents = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp").read()
        cbr_xml = etree.fromstring(contents)
        currency_xml = None
        for e in cbr_xml:
            for p in e:
                if p.tag == 'CharCode' and p.text == currency:
                    currency_xml = e
                    break
            if currency_xml is not None:
                break

        for p in currency_xml:
            if p.tag == 'Value':
                return float(p.text.replace(',', '.'))
    except:
        pass

    return None


def get_comm_type_afy(val):
    """ afy.ru  """
    types = {
        "Помещение под производство ": "manufacturing",
        "ПСН": "free purpose",
        "Офис": "office",
        "ОСЗ": "free purpose",
        "Склад": "warehouse",
        "Бизнес-центр": "office",
        "Торговый центр": "retail",
        "Продажа бизнеса": "business",
        "Готовый бизнес": "business",
    }
    wrong_types = {
        "Дома, Коттеджи, Таунхаусы": "hotel",
        "Гостиничный комплекс ": "hotel",
        "Турбаза": "hotel",
        "Торговая площадь": "land",
        "Общепит": "public catering",
        "Автосервис": "auto repair",
        "Автозаправка": "auto repair",
        "Автомойка": "auto repair",
        "Гараж": "auto repair",
        "Автостоянка ": "auto repair",
        "Усадьба": "hotel",
        "Земля под коммерческую застройку": "land",
        "Земли промназначения": "land",
        "Земли сельхозназначения": "land",
        "Земельные участки под ИЖС": "",
        "Ивестиционный проект": "",
        "Земли сельхозназначения под дачное строительство": "",
        "Квартира": "",
    }

    return types[val]


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

    return types[val]


def get_live_type(native_types):
    if "Дома, Коттеджи, Таунхаусы" in native_types \
            and "Земельные участки под ИЖС" in native_types:
        return "дом с участком"

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

    return types[native_types[0]]


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


def append_location(db, offer, attrs):
    def append_metro(tag, attrs):
        metro_ids = attrs.get('objectMetro', '').split('||')
        time_on_foot = attrs.get('objectDistanceMetro', '')
        if not (attrs.get('objectMetro', '') and time_on_foot):
            return

        for i in [i for key, i in db['metro'].items() if str(key) in metro_ids]:
            yrl_metro = etree.SubElement(tag, 'metro')
            yrl_metro_name = etree.SubElement(yrl_metro, 'name')
            yrl_metro_name.text = i['name']
            yrl_foot_time = etree.SubElement(yrl_metro, 'time-on-foot')
            yrl_foot_time.text = time_on_foot

    yrl_location = etree.SubElement(offer, 'location')

    yrl_country = etree.SubElement(yrl_location, 'country')
    yrl_country.text = 'Россия'

    try:
        region_id = attrs.get('objectRegions', None)
        region = db['regions'][int(region_id)]['name']
        if region.lower() in ['мо', 'подмосковье']:
            region = 'Московская область'
        yrl_region = etree.SubElement(yrl_location, 'region')
        yrl_region.text = region.strip(' ')
    except:
        pass

    if attrs.get('objectLocality', ''):
        city = attrs.get('objectLocality', '').strip(' ')
        yrl_locality = etree.SubElement(yrl_location, 'locality-name')
        yrl_locality.text = city.title()

        region = attrs.get('objectRegionIrr', '').strip(' ').lower()
        if region:
            yrl_region_irr = etree.SubElement(yrl_location, 'district')
            yrl_region_irr.text = region.title()
    elif attrs.get('objectRegionIrr', ''):
        region = attrs.get('objectRegionIrr', '').strip(' ').lower()
        tag = 'district' if 'р-н' in region or 'район' in region else 'locality-name'
        yrl_region_irr = etree.SubElement(yrl_location, tag)
        yrl_region_irr.text = region.title()

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

    if attrs.get('objectDirection', ''):
        for direct in attrs.get('objectDirection', '').split('||'):
            yrl_direct = etree.SubElement(yrl_location, 'direction')
            yrl_direct.text = direct

    if attrs.get('objectDistanceCity', ''):
        yrl_distance = etree.SubElement(yrl_location, 'distance')
        yrl_distance.text = attrs.get('objectDistanceCity', '')

    append_metro(yrl_location, attrs)


def append_sales_agent(db, offer, attrs):
    person_id = attrs.get('objectPerson', '')
    if not person_id:
        return

    yrl_agent = etree.SubElement(offer, 'sales-agent')
    try:
        ptitle = db['content'][int(person_id)]['pagetitle']
    except:
        ptitle = ''
    yrl_name = etree.SubElement(yrl_agent, 'name')
    yrl_name.text = ptitle

    for i in [j for j in db['tmplvarcontentvalues'].values() if j['contentid'] == int(person_id)]:
        templv = db['tmplvars'][i['tmplvarid']]
        if templv['name'] == 'emailPerson':
            yrl_email = etree.SubElement(yrl_agent, 'email')
            yrl_email.text = i['value']
        if templv['name'] == 'phonePerson':
            yrl_phone = etree.SubElement(yrl_agent, 'phone')
            yrl_phone.text = i['value']

    yrl_category = etree.SubElement(yrl_agent, 'category')
    yrl_category.text = 'агентство'

    yrl_organization = etree.SubElement(yrl_agent, 'organization')
    yrl_organization.text = escape('Агентство недвижимости "Мезон"')

    yrl_url = etree.SubElement(yrl_agent, 'url')
    yrl_url.text = 'http://mezonn.ru/'


def append_price(offer, attrs):
    value = attrs.get('object_price', '')
    if not value:
        return

    yrl_price = etree.SubElement(offer, 'price')
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

    value = attrs.get('objectCommission', '')
    if value:
        yrl_commission = etree.SubElement(yrl_price, 'commission')
        yrl_commission.text = value

    value = attrs.get('objectTimeRent', '')
    if value and 'Аренда' == attrs.get('objectType', ''):
        yrl_period = etree.SubElement(yrl_price, 'period')
        yrl_period.text = value


def append_price_domcklick(offer, attrs):
    value = attrs.get('object_price', '')
    if not value:
        return

    yrl_price = etree.SubElement(offer, 'price')
    yrl_value = etree.SubElement(yrl_price, 'value')
    yrl_value.text = value

    yrl_currency = None
    value = attrs.get('objectCurrency', '')
    if value:
        links = {
            'Рубли': 'RUB',
            'Доллары': 'USD',
            'Евро': 'EUR'
        }
        yrl_currency = etree.SubElement(yrl_price, 'currency')
        yrl_currency.text = links[value]

    if yrl_currency is not None and yrl_currency.text != 'RUB':
        try:
            exchange_rate = get_exchange_rate(yrl_currency.text)
            currency_value = exchange_rate * float(yrl_value.text)
            yrl_value.text = str(round(currency_value, -3))
            yrl_currency.text = 'RUB'
        except:
            pass

    value = attrs.get('objectCommission', '')
    if value:
        yrl_commission = etree.SubElement(yrl_price, 'commission')
        yrl_commission.text = value

    value = attrs.get('objectTimeRent', '')
    if value and 'Аренда' == attrs.get('objectType', ''):
        yrl_period = etree.SubElement(yrl_price, 'period')
        yrl_period.text = value


def append_area(offer, attrs):
    if attrs.get('object_area', ''):
        yrl_area = etree.SubElement(offer, 'area')
        yrl_value = etree.SubElement(yrl_area, 'value')
        yrl_value.text = attrs.get('object_area', '')

        yrl_unit = etree.SubElement(yrl_area, 'unit')
        yrl_unit.text = 'кв. м'

    if attrs.get('objectAreaTerritory', ''):
        yrl_lot_area = etree.SubElement(offer, 'lot-area')
        yrl_la_value = etree.SubElement(yrl_lot_area, 'value')
        yrl_la_value.text = attrs.get('objectAreaTerritory', '')
        yrl_la_unit = etree.SubElement(yrl_lot_area, 'unit')
        yrl_la_unit.text = 'сотка'


def generate_object_yrl(db, offer, attrs, for_domcklick=False):
    yrl_type = etree.SubElement(offer, 'type')
    yrl_type.text = 'аренда' if 'Аренда' == attrs.get('objectType', '') else 'продажа'

    yrl_last_update_date = etree.SubElement(offer, 'last-update-date')
    yrl_last_update_date.text = dt.datetime.now().isoformat()

    append_location(db, offer, attrs)
    append_sales_agent(db, offer, attrs)
    append_area(offer, attrs)

    if for_domcklick:
        append_price_domcklick(offer, attrs)
    else:
        append_price(offer, attrs)

    if attrs.get('objectHomeNumberApartment', ''):
        yrl_flat_numb = etree.SubElement(offer, 'apartment')
        yrl_flat_numb.text = attrs.get('objectHomeNumberApartment', '')

    if attrs.get('objectCadastreNumber', ''):
        yrl_cadastr = etree.SubElement(offer, 'cadastral-number')
        yrl_cadastr.text = attrs.get('objectCadastreNumber', '')

    if attrs.get('objectFloor', ''):
        for i in attrs.get('objectFloor', '').replace(' ', '').split(','):
            yrl_floor = etree.SubElement(offer, 'floor')
            yrl_floor.text = i

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

    if attrs.get('content', ''):
        yrl_description = etree.SubElement(offer, 'description')
        yrl_description.text = attrs['content']

    if attrs.get('objectFurniture', ''):
        yrl_furniture = etree.SubElement(offer, 'room-furniture')
        yrl_furniture.text = 'да'

    if attrs.get('objectPlumbing', ''):
        yrl_water = etree.SubElement(offer, 'water-supply')
        yrl_water.text = 'да'

    if attrs.get('objectSewerage', ''):
        yrl_sewerage = etree.SubElement(offer, 'sewerage-supply')
        yrl_sewerage.text = 'да'

    if attrs.get('objectElectricity', ''):
        yrl_electro = etree.SubElement(offer, 'electricity-supply')
        yrl_electro.text = 'да'

    if attrs.get('objectGaz', ''):
        yrl_gas = etree.SubElement(offer, 'gas-supply')
        yrl_gas.text = 'да'

    if attrs.get('objectHeating', ''):
        yrl_gas = etree.SubElement(offer, 'heating-supply')
        yrl_gas.text = 'да'


def add_extra_commercial(db, offer, attrs, for_afy):
    yrl_category = etree.SubElement(offer, 'category')
    yrl_category.text = 'коммерческая'

    yrl_deal_status = etree.SubElement(offer, 'deal-status')
    yrl_deal_status.text = 'direct rent'

    if attrs.get('object-objectspecies', ''):
        types = []
        for i in attrs.get('object-objectspecies', '').split('||'):
            if for_afy:
                comm_type = get_comm_type_afy(db['objectspecies'][i]['name'])
            else:
                comm_type = get_comm_type(db['objectspecies'][i]['name'])
            if not comm_type or comm_type in types:
                continue
            types.append(comm_type)

            yrl_commercial_type = etree.SubElement(offer, 'commercial-type')
            yrl_commercial_type.text = comm_type
            break


def add_extra_living(db, offer, attrs):
    yrl_deal_status = etree.SubElement(offer, 'property-type')
    yrl_deal_status.text = 'жилая'

    yrl_deal_status = etree.SubElement(offer, 'deal-status')
    yrl_deal_status.text = 'sale'

    if attrs.get('objectFloorAll', ''):
        yrl_floors_all = etree.SubElement(offer, 'floors-total')
        yrl_floors_all.text = attrs.get('objectFloorAll', '')

    if attrs.get('objectHomeHousing', ''):
        yrl_floors_all = etree.SubElement(offer, 'building-section')
        yrl_floors_all.text = attrs.get('objectHomeHousing', '')

    if attrs.get('objectCountRoom', ''):
        yrl_rooms = etree.SubElement(offer, 'rooms-offered')
        yrl_rooms.text = attrs.get('objectCountRoom', '')

    if attrs.get('objectAreaLive', ''):
        yrl_live_space = etree.SubElement(offer, 'living-space')
        yrl_ls_value = etree.SubElement(yrl_live_space, 'value')
        yrl_ls_value.text = attrs.get('objectAreaLive', '')
        yrl_ls_unit = etree.SubElement(yrl_live_space, 'unit')
        yrl_ls_unit.text = 'кв. м'

    if attrs.get('objectAreaKitchen', ''):
        yrl_kitchen_space = etree.SubElement(offer, 'kitchen-space')
        yrl_ks_value = etree.SubElement(yrl_kitchen_space, 'value')
        yrl_ks_value.text = attrs.get('objectAreaKitchen', '')
        yrl_ks_unit = etree.SubElement(yrl_kitchen_space, 'unit')
        yrl_ks_unit.text = 'кв. м'

    if attrs.get('objectAreaAllRoom', ''):
        for i in re.split('[-/]', attrs.get('objectAreaAllRoom', '')):
            i = i.strip()
            if not i:
                continue
            yrl_room_space = etree.SubElement(offer, 'room-space')
            yrl_rs_value = etree.SubElement(yrl_room_space, 'value')
            yrl_rs_value.text = i
            yrl_rs_unit = etree.SubElement(yrl_room_space, 'unit')
            yrl_rs_unit.text = 'кв. м'

    if attrs.get('object-objectspecies', ''):
        types = [db['objectspecies'][i]['name'] for i in
            attrs.get('object-objectspecies', '').split('||')
        ]
        try:
            cat = get_live_type(types)
            yrl_category = etree.SubElement(offer, 'category')
            yrl_category.text = cat
        except:
            pass


def generate_yrl(db, for_afy=False, only_flats=False, for_domcklick=False):
    # Create root element
    xml = etree.Element('realty-feed', xmlns="http://webmaster.yandex.ru/schemas/feed/realty/2010-06")
    date_element = etree.SubElement(xml, 'generation-date')
    date_element.text = str(dt.datetime.now().isoformat())
    for content_id, content in db['content'].items():
        # skip if not in 'object' folder and
        # 10 - is realty object template ID
        # 326 - id of 'Objects' folder (see manage site)
        if content['template'] != 10 or content['parent'] != 326:
            continue

        attrs = {
            'content': content['content']
        }
        obj_type = ''
        for tmplvarid, value in [(i['tmplvarid'], i['value']) for i in db['tmplvarcontentvalues'].values() if i['contentid'] == content_id]:
            templv = db['tmplvars'][tmplvarid]
            if templv['name'] == 'objectTypeS':
                obj_type = value
                continue
            attrs[templv['name']] = value

        # Check only flats flag
        if only_flats and obj_type != 'Квартиры':
            continue

        if for_domcklick:
            if obj_type != 'Квартиры':
                continue
            if 'Аренда' == attrs.get('objectType', ''):
                continue

        # skip object if field 'LoadXML' is set to 0
        if attrs.get('objectLoadXML', '1') != '1':
            continue

        offer = etree.SubElement(xml, 'offer', **{'internal-id': str(content_id)})
        try:
            yrl_creation_date = etree.SubElement(offer, 'creation-date')
            if content['publishedon']:
                yrl_creation_date.text = dt.datetime.fromtimestamp(int(content['publishedon'])).isoformat()
            else:
                yrl_creation_date.text = timezone.now().isoformat()

            # проверка площади - если больше 100 соток, то автоматом коммерческая
            auto_commerc = False
            lot_area = attrs.get('objectAreaTerritory', None)
            try:
                avail_types = ['Загородная недвижимость', 'Квартиры', 'Коммерческая недвижимость']
                if int(lot_area) >= 100 and obj_type in avail_types:
                    auto_commerc = True
                    # изменяем параметры под требования коммерческой недвижимости
                    attrs['object-objectspecies'] = '17'
            except:
                pass

            generate_object_yrl(db, offer, attrs, for_domcklick)
            if auto_commerc or obj_type == 'Коммерческая недвижимость':
                add_extra_commercial(db, offer, attrs, for_afy)
            elif obj_type in ['Загородная недвижимость', 'Квартиры']:
                add_extra_living(db, offer, attrs)
        except:
            offer.getparent().remove(offer)

    task_key = keys.DEFAULT
    if for_afy:
        task_key = keys.AFY
    if only_flats:
        task_key = keys.ONLY_FLATS
    if for_domcklick:
        task_key = keys.DOMCKLICK

    task_res, created = XmlFeed.objects.get_or_create(task_key=task_key)
    task_res.content = etree.tostring(xml, encoding='UTF-8', xml_declaration=True)
    task_res.save(using='default')


def get_yrl():
    db = download_data()
    generate_yrl(db)
    generate_yrl(db, for_afy=True)
    generate_yrl(db, only_flats=True)
    generate_yrl(db, for_domcklick=True)
