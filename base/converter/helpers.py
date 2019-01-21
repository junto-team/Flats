import requests
from lxml import etree

from django.core.cache import cache
from base.models import *

db = None


def download_data():
    global db

    if db is not None:
        return db

    db = {
        'content': {i['id']: {
            'content': i['content'],
            'publishedon': i['publishedon'],
            'parent': i['parent'],
            'pagetitle': i['pagetitle'],
            'template': i['template']
        } for i in AnysiteSiteContent.objects.using('mezon').values('id', 'content', 'parent', 'publishedon', 'pagetitle', 'template')},
        'tmplvarcontentvalues': {i['id']: {
            'contentid': i['contentid'],
            'tmplvarid': i['tmplvarid'],
            'value': i['value']
        } for i in AnysiteSiteTmplvarContentvalues.objects.using('mezon').all().values('id', 'contentid', 'tmplvarid', 'value')},
        'tmplvars': {i['id']: {
            'name': i['name']
        } for i in AnysiteSiteTmplvars.objects.using('mezon').all().values('id', 'name')},
        'regions': {i['id']: {
            'name': i['name']
        } for i in AnysiteRegions.objects.using('mezon').all().values('id', 'name')},
        'metro': {i['id']: {
            'name': i['name']
        } for i in AnysiteMetro.objects.using('mezon').all().values('id', 'name')},
        'objectspecies': {str(i['id']): {
            'name': i['name']
        } for i in AnysiteObjectspecies.objects.using('mezon').all().values('id', 'name')}
    }
    return db


def cian_get_highway(name):
    # download cian xml with highway's IDs
    cian_highway = cache.get('cian_highway')
    if not cian_highway:
        r = requests.get("https://www.cian.ru/highways.xml")
        r.encoding = 'utf-8'
        cian_highway = r.text.encode('utf-8')
        cache.set('cian_highway', cian_highway, 60 * 60 * 24 * 7)
    highway_tree = etree.fromstring(cian_highway)

    # find name in highways
    name = name.lower()
    for highway in highway_tree:
        if highway.text.lower() in name:
            return highway.attrib['id']

    return ''


def cian_get_metro(name):
    # download cian xml with metro's IDs
    cian_metro = cache.get('cian_metro')
    if not cian_metro:
        r = requests.get("https://www.cian.ru/metros-moscow.xml")
        r.encoding = 'utf-8'
        cian_metro = r.text.encode('utf-8')
        cache.set('cian_metro', cian_metro, 60 * 60 * 24 * 7)
    metro_tree = etree.fromstring(cian_metro)

    # find name in metro
    name = name.lower()
    for metro in metro_tree:
        if metro.text.lower() in name:
            return metro.attrib['id']

    return ''
