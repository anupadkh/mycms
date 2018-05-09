from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<person_id>[0-9]+)/$', views.detail, name='detail'),
    path('<int:person_id>/', views.detail, name='vote'),
]

#Namespacing URL Names
app_name = "personal"
