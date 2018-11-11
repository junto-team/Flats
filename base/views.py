from django.http import HttpResponse

from .models import XmlFeed
from .converter import keys, yandex, cian


def yrl(request):
    try:
        task_result = XmlFeed.objects.using('default').get(task_key=keys.DEFAULT)
        xml = task_result.content
    except:
        yandex.get_yrl()
        cian.get_yrl()
        task_result = XmlFeed.objects.using('default').get(task_key=keys.DEFAULT)
        xml = task_result.content

    return HttpResponse(
        xml,
        content_type="application/xml"
    )


def yrl_afy(request):
    try:
        task_result = XmlFeed.objects.using('default').get(task_key=keys.AFY)
        xml = task_result.content
    except:
        yandex.get_yrl()
        task_result = XmlFeed.objects.using('default').get(task_key=keys.AFY)
        xml = task_result.content

    return HttpResponse(
        xml,
        content_type="application/xml"
    )


def yrl_flats(request):
    try:
        task_result = XmlFeed.objects.using('default').get(task_key=keys.ONLY_FLATS)
        xml = task_result.content
    except:
        yandex.get_yrl()
        task_result = XmlFeed.objects.using('default').get(task_key=keys.ONLY_FLATS)
        xml = task_result.content

    return HttpResponse(
        xml,
        content_type="application/xml"
    )


def yrl_domklick(request):
    try:
        task_result = XmlFeed.objects.using('default').get(task_key=keys.DOMCKLICK)
        xml = task_result.content
    except:
        yandex.get_yrl()
        task_result = XmlFeed.objects.using('default').get(task_key=keys.DOMCKLICK)
        xml = task_result.content

    return HttpResponse(
        xml,
        content_type="application/xml"
    )


def feed_cian(request):
    try:
        task_result = XmlFeed.objects.using('default').get(task_key=keys.CIAN)
        xml = task_result.content
    except:
        cian.get_yrl()
        task_result = XmlFeed.objects.using('default').get(task_key=keys.CIAN)
        xml = task_result.content

    return HttpResponse(
        xml,
        content_type="application/xml"
    )


def manual_yrl(request):
    yandex.get_yrl()
    cian.get_yrl()
    task_result = XmlFeed.objects.using('default').get(task_key=200)

    return HttpResponse(
        task_result.content,
        content_type="application/xml"
    )
