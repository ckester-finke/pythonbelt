from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^home$', views.home),
    url(r'^logout$', views.logout),
    url(r'^add/(?P<user_id>\w+)$', views.add),
    url(r'^remove/(?P<user_id>\w+)$', views.remove),
    url(r'^friend/(?P<user_id>\w+)$', views.display),
]