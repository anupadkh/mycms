from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^datamode/$', views.entry, name='entry'),
    # url(r'^datamode/<int:person>/person/(?P<house>[0-9]+)/$', views.entry, name='personid'),
    path('datamode/<int:person>/person/', views.entry, name='personid'),
    url(r'^people/$', views.all_people, name='people'),
    # url(r'^(?P<person_id>[0-9]+)/$', views.detail, name='detail'),
        path('people/<int:status>/stat/', views.all_people, name='people_status'),
        path('people/<int:id>/<int:pt>/address', views.address_entry, name='address_entry'),
        path('people/<int:id>/<int:card>/card', views.card_entry, name='card_details'),
        path('people/<int:id>/<int:contact>/contact', views.contact_entry, name='contact_details'),
        path('people/<int:id>/<int:media>/media', views.social_entry, name='social_details'),
        path('people/<int:id>/hobby', views.hobby_entry, name='hobby'),

    path('geo/<int:id>/', views.geo_entry, name='geo'),
        path('house/<int:geo>/<int:pid>/house/',views.house_entry, name='house_entry'),
            path('house/<int:coordinates>/<int:pid>/head/', views.house_head_entry, name='house_head'),
        path('family/<int:house>/<int:fid>/family/<int:geo>/coordinates/<int:pid>/person', views.family_entry, name='family_details'),
        path('relation/<int:mooli>/<int:child>/<int:entry>/', views.relation_entry, name='relation'),
    # # path('')

    path('family/<int:geo>/coordinate/',views.family_list,name='family_list'),
    path('family/<int:family_id>/members', views.member_list, name="memberlist"),

]

#Namespacing URL Names
app_name = "formentry"
