from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path('form', views.form_view, name='form_view'),
    path('home', views.home_view, name='home_view'),


]
