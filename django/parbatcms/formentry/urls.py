from django.conf.urls import url
from django.urls import path

from . import views
from . import formviews

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
        path('people/<int:id>/<int:hobby>/hobby', views.hobby_entry, name='hobby'),

    path('geo/<int:id>/', views.geo_entry, name='geo'),
        path('house/<int:geo>/<int:pid>/house/',views.house_entry, name='house_entry'),
            path('house/<int:coordinates>/<int:pid>/head/', views.house_head_entry, name='house_head'),
        path('family/<int:house>/<int:fid>/family/<int:geo>/coordinates/<int:pid>/person', views.family_entry, name='family_details'),
        path('relation/<int:mooli>/<int:child>/<int:entry>/', views.relation_entry, name='relation'),
    # # path('')

    path('family/<int:geo>/coordinate/',views.family_list,name='family_list'),
    path('family/<int:family_id>/members', views.member_list, name="memberlist"),

    path('myform/<int:form_id>/member/<int:member>/marktype/<int:mark>/<int:marker>/', formviews.mainforms, name='form_basic'),
    path('myform/all_forms', formviews.all_my_forms, name='all_my_forms'),
    path('userforms/<int:member>/type/<int:memtype>', formviews.all_member_forms, name='memberforms'),

    url(r'^design/$', formviews.index, name='form_index'),
    path('design/<int:id>/main/', formviews.formindex, name='submit_formindex'),
    path('design/<int:id>/table/', formviews.tableindex, name='table_index'),
    path('design/<int:formid>/form/<int:tid>/mytable/', formviews.submit_tableindex, name='submit_tableindex'),
    path('design/<int:id>/question/', formviews.questionindex, name='question_index'),
    path('design/<int:tid>/table/<int:qid>/myquestion/', formviews.submit_questionindex, name='submit_questionindex'),
    path('design/<int:id>/choice/', formviews.choiceindex, name='choice_index'),
    path('design/<int:qid>/question/<int:cid>/mychoice/', formviews.submit_choiceindex, name='submit_choiceindex'),
]

#Namespacing URL Names
app_name = "formentry"
