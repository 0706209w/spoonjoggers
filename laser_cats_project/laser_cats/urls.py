from django.conf.urls import patterns, url
from laser_cats import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^add_animalprofile/$', views.add_AnimalProfile, name='add_AnimalProfile',),
        url(r'^animalprofile/(?P<animalprofile_name_slug>[\w\-]+)/$', views.AnimalProfile, name = 'animal profile'),
        url(r'^add_picture/$', views.add_Picture, name='add_Picture'),
        )