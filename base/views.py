from django.http import HttpResponse

from base.models import CeleryResults
from .tasks import task_get_yrl


def yrl(request):
    try:
        task_result = CeleryResults.objects.using('default').get(task_key=200)
        xml = task_result.content
    except:
        task_get_yrl.apply()
        task_result = CeleryResults.objects.using('default').get(task_key=200)
        xml = task_result.content

    return HttpResponse(
        xml,
        content_type="application/xml"
    )


def manual_yrl(request):
    task_get_yrl.apply()
    task_result = CeleryResults.objects.using('default').get(task_key=200)

    return HttpResponse(
        task_result.content,
        content_type="application/xml"
    )
