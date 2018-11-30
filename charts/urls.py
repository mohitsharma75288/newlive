from . import views
from django.conf.urls import url, include

app_name = 'charts'

urlpatterns=[
  url('', views.index, name='index'),
  ]