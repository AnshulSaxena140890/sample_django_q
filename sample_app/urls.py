from django.urls import path, re_path
from sample_app import views

app_name = "article"
urlpatterns = [

    re_path(r'^django-q/(?P<category>[\w-]+)/(?P<count>[0-9]{1})/$', views.RunDjangoQView.as_view(), name='django_q_sample')

]