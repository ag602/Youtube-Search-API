from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='index'),
    ]