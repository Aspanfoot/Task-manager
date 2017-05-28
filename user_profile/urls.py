from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
	url(r'^$', views.profile, name = 'home'),
	url(r'^tasks/$', views.tasks, name = 'tasks' ),
	url(r'^tasks/add/$', views.add_task, name = 'add_task'),
	url(r'^tasks/(?P<pk>\d+)/update/$', views.update_task, name = 'update_task'),
	url(r'^tasks/(?P<pk>\d+)/delete/$', views.delete_task, name = 'delete_task'),
]