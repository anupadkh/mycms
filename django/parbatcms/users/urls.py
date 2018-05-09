from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    # url(r'^(?P<person_id>[0-9]+)/$', views.detail, name='detail'),
    # path('<int:person_id>/', views.detail, name='vote'),
]

#Namespacing URL Names
app_name = "users"
