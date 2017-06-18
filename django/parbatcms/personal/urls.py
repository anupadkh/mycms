from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # ex: /polls/
    url(r'^$', views.index, name='index'),

]

#Namespacing URL Names
app_name = "personal"
