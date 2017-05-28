"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from registration.forms import RegistrationFormUniqueEmail
from registration.backends.simple.views import RegistrationView
from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^home/',views.home, name = 'home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/', RegistrationView.as_view(form_class = RegistrationFormUniqueEmail),
           name = 'unique_email_register'),
    url(r'^accounts/', include('registration.backends.simple.urls' , namespace = 'accounts')),
    url(r'^accounts/profile/', include('user_profile.urls', namespace = 'profile')),
]
