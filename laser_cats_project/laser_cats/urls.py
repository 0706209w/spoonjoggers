from django.conf.urls import patterns, url
from laser_cats import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))