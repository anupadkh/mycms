from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^datamode/$', views.entry, name='entry'),
    path('datamode/<int:person>/person/', views.entry, name='personid'),
    url(r'^people/$', views.all_people, name='people'),
    # url(r'^(?P<person_id>[0-9]+)/$', views.detail, name='detail'),
    path('people/<int:status>/stat/', views.all_people, name='people_status'),
    # path('<int:person_id>/', views.detail, name='vote'),
]

#Namespacing URL Names
app_name = "formentry"
