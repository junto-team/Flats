from lxml import etree
import json
import re

from base.models import *
from base.converter.helpers import download_data, cian_get_highway, \
    cian_get_metro
from base.converter import keys

home_types = {
    'aerocreteBlock': 'Газобетонный блок',
    'block': 'Блочный',
    'boards': 'Щитовой',
    'brick': 'Кирпичный',
    'foamConcreteBlock': 'Пенобетонный блок',
    'gasSilicateBlock': 'Газосиликатный блок',
    'monolith': 'Монолитный',
    'monolithBrick': 'Кирпично-монолитный',
    'old': 'Старый фонд',
    'panel': 'Панельный',
    'stalin': 'Сталинский',
    'wireframe': 'Каркасный',
    'wood': 'Деревянный',
}

parking_types = {
    'Наземная': "ground",
    'Многоуровневая': "multilevel",
    'Подземная': "underground",
    'На крыше': "roof",
}


def get_home_type(name):
    for k,v in home_types.items():
        if name.lower().strip() == v.lower():
            return k
    return ''


def get_boolean(attrs, name):
    return 'true' if attrs.get(name, None) else 'false'


def append_building(attrs, root_tag):
    building = etree.SubElement(root_tag, 'Building')

    if attrs.get('objectNameBuilding', ''):
        name = etree.SubElement(building, 'Name')
        name.text = attrs.get('objectNameBuilding', '')

    new_tag = etree.SubElement(building, 'FloorsCount')
    new_tag.text = attrs.get('objectFloorAll', '')

    if attrs.get('objectYearBuilding', ''):
        new_tag = etree.SubElement(building, 'BuildYear')
        new_tag.text = attrs.get('objectYearBuilding', '')

    home_type = get_home_type(attrs.get('objectHomeType', ''))
    if home_type:
        new_attr = etree.SubElement(building, 'MaterialType')
        new_attr.text = home_type

    if attrs.get('objectHeightRoof', ''):
        new_tag = etree.SubElement(building, 'CeilingHeight')
        new_tag.text = attrs.get('objectHeightRoof', '')

    if attrs.get('objectLiftPassenger', ''):
        new_tag = etree.SubElement(building, 'PassengerLiftsCount')
        new_tag.text = attrs.get('objectLiftPassenger', '')

    if attrs.get('objectLiftCargo', ''):
        new_tag = etree.SubElement(building, 'CargoLiftsCount')
        new_tag.text = attrs.get('objectLiftCargo', '')

    new_tag = etree.SubElement(building, 'HasGarbageChute')
    new_tag.text = get_boolean(attrs, 'objectHaveChute')

    parking = etree.SubElement(building, 'Parking')
    parking_type = etree.SubElement(parking, 'Type')
    parking_type.text = parking_types.get(attrs.get('objectParking', ''), 'ground')


def append_bargain_rent(attrs, root_tag):
    bargain_tag = etree.SubElement(root_tag, 'BargainTerms')

    value = attrs.get('object_price', '')
    if not value:
        return

    price = etree.SubElement(bargain_tag, 'Price')
    price.text = value

    value = attrs.get('objectCurrency', '')
    if value:
        links = {
            'Рубли': 'RUB',
            'Доллары': 'USD',
            'Евро': 'EUR'
        }
        yrl_currency = etree.SubElement(bargain_tag, 'Currency')
        yrl_currency.text = links[value]

    price = etree.SubElement(bargain_tag, 'LeaseTermType')
    price.text = 'fewMonths'

    value = attrs.get('objectCommission', '')
    if value:
        agent_bonus = etree.SubElement(bargain_tag, 'AgentBonus')
        bouns_value = etree.SubElement(agent_bonus, 'Value')
        bouns_value.text = value
        ptype = etree.SubElement(agent_bonus, 'PaymentType')
        ptype.text = 'percent'


def append_bargain_sale(attrs, root_tag):
    bargain_tag = etree.SubElement(root_tag, 'BargainTerms')

    value = attrs.get('object_price', '')
    if not value:
        return

    price = etree.SubElement(bargain_tag, 'Price')
    price.text = value

    value = attrs.get('objectCurrency', '')
    if value:
        links = {
            'Рубли': 'RUB',
            'Доллары': 'USD',
            'Евро': 'EUR'
        }
        yrl_currency = etree.SubElement(bargain_tag, 'Currency')
        yrl_currency.text = links[value]

    price = etree.SubElement(bargain_tag, 'SaleType')
    price.text = 'free'

    value = attrs.get('objectCommission', '')
    if value:
        agent_bonus = etree.SubElement(bargain_tag, 'AgentBonus')
        value = etree.SubElement(agent_bonus, 'Value')
        value.text = value
        ptype = etree.SubElement(agent_bonus, 'PaymentType')
        ptype.text = 'percent'


def generate_object_yrl(attrs, root_tag):
    flat_rooms_count = etree.SubElement(root_tag, 'FlatRoomsCount')
    flat_rooms_count.text = attrs.get('objectCountRoom', '')

    apartments = etree.SubElement(root_tag, 'IsApartments')
    apartments.text = get_boolean(attrs, 'objectApartments')

    penthouse = etree.SubElement(root_tag, 'IsPenthouse')
    penthouse.text = get_boolean(attrs, 'objectPenthouse')

    total_area = etree.SubElement(root_tag, 'TotalArea')
    total_area.text = attrs.get('object_area', '')

    floor_number = etree.SubElement(root_tag, 'FloorNumber')
    floor_number.text = attrs.get('objectFloor', '')

    rooms_area = etree.SubElement(root_tag, 'AllRoomsArea')
    rooms_area.text = attrs.get('objectAreaAllRoom', '').replace('/', '+')

    new_attr = etree.SubElement(root_tag, 'LivingArea')
    new_attr.text = attrs.get('objectAreaLive', '')

    new_attr = etree.SubElement(root_tag, 'KitchenArea')
    new_attr.text = attrs.get('objectKitchen', '')

    new_attr = etree.SubElement(root_tag, 'LoggiasCount')
    new_attr.text = attrs.get('objectLoggia', '')

    new_attr = etree.SubElement(root_tag, 'BalconiesCount')
    new_attr.text = attrs.get('objectBalcony', '')

    new_attr = etree.SubElement(root_tag, 'WindowsViewType')
    if attrs.get('objectViewStreet', '') == 'Да' and attrs.get('objectViewYard', '') == 'Да':
        new_attr.text = 'yardAndStreet'
    elif attrs.get('objectViewStreet', '') == 'Да':
        new_attr.text = 'street'
    else:
        new_attr.text = 'yard'

    new_attr = etree.SubElement(root_tag, 'SeparateWcsCount')
    new_attr.text = attrs.get('objectSeparateToilet', '')

    new_attr = etree.SubElement(root_tag, 'CombinedWcsCount')
    new_attr.text = attrs.get('objectCombineToilet', '')

    new_attr = etree.SubElement(root_tag, 'RepairType')
    if attrs.get('objectRepair', '') == 'Без ремонта':
        new_attr.text = 'no'
    if attrs.get('objectRepair', '') == 'Косметический ремонт':
        new_attr.text = 'cosmetic'
    if attrs.get('objectRepair', '') == 'Капитальный ремонт':
        new_attr.text = 'design'
    if attrs.get('objectRepair', '') == 'Евро-ремонт':
        new_attr.text = 'euro'

    new_attr = etree.SubElement(root_tag, 'HasFurniture')
    new_attr.text = 'false' if attrs.get('objectFurniture', 'Нет') == 'Нет' else 'true'

    new_attr = etree.SubElement(root_tag, 'HasPhone')
    new_attr.text = get_boolean(attrs, 'objectHavePhone')

    new_attr = etree.SubElement(root_tag, 'HasRamp')
    new_attr.text = get_boolean(attrs, 'objectHaveRamp')

    append_building(attrs, root_tag)


def generate_for_rent(attrs, root_tag):
    category = etree.SubElement(root_tag, 'Category')
    category.text = 'flatRent'

    append_bargain_rent(attrs, root_tag)


def generate_for_sale(attrs, root_tag):
    category = etree.SubElement(root_tag, 'Category')
    category.text = 'flatSale'

    append_bargain_sale(attrs, root_tag)


def get_agent_number(db, attrs):
    """ Return agent number by specified object's attributes """
    person_id = attrs.get('objectPerson', '')
    if not person_id:
        return

    number = None
    for i in [j for j in db['tmplvarcontentvalues'].values() if j['contentid'] == int(person_id)]:
        templv = db['tmplvars'][i['tmplvarid']]
        if templv['name'] == 'phonePersonCian':
            number = i['value']
            break

        if templv['name'] == 'phonePerson':
            number = i['value']

    if not number:
        return None

    # save only digits without country code
    number = re.sub('[^0-9]', '', number)[-10:]
    return number


def append_agent(db, attrs, root_tag):
    """ Append agent by specified object's attributes """
    person_id = attrs.get('objectPerson', '')
    if not person_id:
        return

    sub_agent = etree.SubElement(root_tag, 'SubAgent')
    try:
        ptitle = db['content'][int(person_id)]['pagetitle']
    except:
        ptitle = 'No Name'
    ptitle = ptitle.split(' ')

    first_name = etree.SubElement(sub_agent, 'FirstName')
    first_name.text = ptitle[0]
    last_name = etree.SubElement(sub_agent, 'LastName')
    last_name.text = ptitle[1]
    avatar_url = etree.SubElement(sub_agent, 'AvatarUrl')
    avatar_url.text = 'http://mezonn.ru/img/logo.png'

    for i in [j for j in db['tmplvarcontentvalues'].values() if
              j['contentid'] == int(person_id)]:
        templv = db['tmplvars'][i['tmplvarid']]
        if templv['name'] == 'emailPerson':
            email = etree.SubElement(sub_agent, 'Email')
            email.text = i['value']
        if templv['name'] == 'phonePerson':
            phone = etree.SubElement(sub_agent, 'Phone')
            phone.text = i['value']


def append_metro(db, attrs, root_tag):
    metro_ids = attrs.get('objectMetro', '').split('||')
    time_on_foot = attrs.get('objectDistanceMetro', '')
    if not (attrs.get('objectMetro', '') and time_on_foot):
        return

    # split time for every station
    time_on_foot = time_on_foot.split(',')

    counter = 0
    undergrounds = etree.SubElement(root_tag, 'Undergrounds')
    for i in [i for key, i in db['metro'].items() if str(key) in metro_ids]:
        counter += 1
        if counter > 3:
            break
        underground_schema = etree.SubElement(undergrounds, 'UndergroundInfoSchema')
        transport_type = etree.SubElement(underground_schema, 'TransportType')
        transport_type.text = 'walk'
        time = etree.SubElement(underground_schema, 'Time')
        try:
            time.text = time_on_foot[counter - 1]
        except:
            time.text = time_on_foot[0]
        metro_id = etree.SubElement(underground_schema, 'Id')
        metro_id.text = cian_get_metro(i['name'])


def generate_yrl(db):
    # Create root element
    xml = etree.Element('feed')
    feed_version = etree.SubElement(xml, 'feed_version')
    feed_version.text = '2'
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

        if obj_type != 'Квартиры':
            continue

        # skip object if field 'LoadCian' is set to 0
        if attrs.get('objectLoadCian', '1') != '1':
            continue

        offer = etree.SubElement(xml, 'object')
        try:
            external_id = etree.SubElement(offer, 'ExternalId')
            external_id.text = str(content_id)

            description = etree.SubElement(offer, 'Description')
            description.text = attrs.get('content', "")

            address = etree.SubElement(offer, 'Address')
            address.text = attrs.get('object-address', "")

            if attrs.get('objectCadastreNumber', None):
                address = etree.SubElement(offer, 'CadastralNumber')
                address.text = attrs.get('objectCadastreNumber', "")

            phone = etree.SubElement(offer, 'Phones')
            phone_schema = etree.SubElement(phone, 'PhoneSchema')
            country_code = etree.SubElement(phone_schema, 'CountryCode')
            country_code.text = '+7'
            number = etree.SubElement(phone_schema, 'Number')
            number.text = get_agent_number(db, attrs)

            highway = etree.SubElement(offer, 'Highway')
            distance = etree.SubElement(highway, 'Distance')
            distance.text = '1'  # TODO: add real distance
            highway_id = etree.SubElement(highway, 'Id')
            highway_id.text = cian_get_highway(attrs.get('objectHighway', ""))

            append_metro(db, attrs, offer)
            append_agent(db, attrs, offer)

            # append photos
            images = json.loads(attrs.get('object-images', ''))
            photos = etree.SubElement(offer, 'Photos')
            for i in images:
                url = 'http://mezonn.ru/template/images/{}'.format(i['image'])
                photo_schema = etree.SubElement(photos, 'PhotoSchema')
                full_url = etree.SubElement(photo_schema, 'FullUrl')
                full_url.text = url
                is_default = etree.SubElement(photo_schema, 'IsDefault')
                is_default.text = 'false'

            generate_object_yrl(attrs, offer)
            if 'Аренда' == attrs.get('objectType', ''):
                generate_for_rent(attrs, offer)
            else:
                generate_for_sale(attrs, offer)
        except:
            offer.getparent().remove(offer)

    task_res, created = XmlFeed.objects.get_or_create(task_key=keys.CIAN)
    task_res.content = etree.tostring(xml, encoding='UTF-8', xml_declaration=True)
    task_res.save(using='default')


def get_yrl():
    db = download_data()
    generate_yrl(db)
