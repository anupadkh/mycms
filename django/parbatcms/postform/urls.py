from django.conf.urls import url
from django.urls import path
from photouploads import photoviews
from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # url(r'^datamode/$', views.entry, name='entry'),
    path('data', views.makePost, name='saveposts'),
    path('design/test', views.seePost, name="seepost"),
    path('uploads/<int:member>/<int:memberType>', photoviews.simple_upload, name="upload")
]

#Namespacing URL Names
app_name = "postform"
