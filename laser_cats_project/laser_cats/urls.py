from django.conf.urls import patterns, url
from laser_cats import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^add_animalprofile/$', views.add_AnimalProfile, name='add_AnimalProfile',),
        url(r'^animalprofile/(?P<animalprofile_name_slug>[\w\-]+)/$', views.animalprofile, name = 'animal profile'),
        url(r'^add_picture/(?P<animalprofile_name_slug>[\w\-]+)/$', views.add_Picture, name='add_Picture'),
        url(r'^register/$', views.register, name = 'register'),
        url(r'^login/$', views.user_login, name = 'login'),
        url(r'^restricted/', views.restricted, name = 'restricted'),
        url(r'^logout/$', views.user_logout, name = 'logout'),
        )