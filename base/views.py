from django.http import HttpResponse

from base.models import CeleryResults
from .tasks import get_yrl


def yrl(request):
    try:
        task_result = CeleryResults.objects.using('default').get(task_key=200)
        xml = task_result.content
    except:
        get_yrl.apply()
        task_result = CeleryResults.objects.using('default').get(task_key=200)
        xml = task_result.content

    return HttpResponse(
        xml,
        content_type="application/xml"
    )


def manual_yrl(request):
    get_yrl.apply()
    task_result = CeleryResults.objects.using('default').get(task_key=200)
    CeleryResults.objects.using('default').get(task_key=200).delete()

    return HttpResponse(
        task_result.content,
        content_type="application/xml"
    )
