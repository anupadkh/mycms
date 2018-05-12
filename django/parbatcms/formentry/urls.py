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
    # path('people/<int:id>/<int:pt>/<int:address>/address', views.address, name='address'),
    # path('people/<int:id>/<int:card>/card', views.card, name='card_details'),
    # path('people/<int:id>/<int:contact>/contact', views.contact, name='contact'),
    # path('people/<int:id>/<int:type>/media', views.social_media, name='social'),
    # path('people/<int:id>/<int:hobby>/hobby', views.hobby_view, name='hobby'),
    #
    path('geo/<int:id>/', views.geo_entry, name='geo')
    # path('house/<int:geo>/<int:house>/<int:person>',views.house_entry, name='house'),
    # path('family/<int:house>/<int:family>/<int:person>', views.family_entry, name='family'),
    # path('relation/<int:mooli>/<int:child>', views.relation_entry, name='relation'),
    # # path('')

]

#Namespacing URL Names
app_name = "formentry"
