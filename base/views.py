from django.http import HttpResponse

from .models import XmlFeed
from .converter import get_yrl


def yrl(request):
    try:
        task_result = XmlFeed.objects.using('default').get(task_key=200)
        xml = task_result.content
    except:
        get_yrl()
        task_result = XmlFeed.objects.using('default').get(task_key=200)
        xml = task_result.content

    return HttpResponse(
        xml,
        content_type="application/xml"
    )


def manual_yrl(request):
    get_yrl()
    task_result = XmlFeed.objects.using('default').get(task_key=200)

    return HttpResponse(
        task_result.content,
        content_type="application/xml"
    )
