from sample_app.models import Category
from django_q.tasks import async_task
from django.http import HttpResponse
import random


def add_django_queue_task(request, category, count):
    # category = request.GET.get('category')
    # count = request.GET.get('count')
    objects_count = int(count)

    while objects_count > 0:
        async_task('sample_app.handlers.common_function',
                   category
                   )
        objects_count -= 1

    return HttpResponse('Success')


def common_function(category):
    if category is not None:
        category_object = Category(
            name=str(category) + str(random.randint(1, 9))
        )
        category_object.save()
