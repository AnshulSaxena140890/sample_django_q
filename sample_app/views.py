from django.shortcuts import render
from django.views.generic import View
import sample_app.handlers as sample_app_handlers

# Create your views here.


class RunDjangoQView(View):
    def get(self, request, *args, **kwargs):
        return sample_app_handlers.add_django_queue_task(request,
                                                         category=kwargs['category'],
                                                         count=kwargs['count']
                                                         )
