# from django.contrib import admin
# from django.urls import path

# from . import views

# urlpatterns = [
    # path("", views.index),
#     path('form', views.form_view, name='form_view'),
#     path('home', views.home_view, name='home_view'),
#     path('users', views.users_view, name='users_view'),
# ]

from django.urls import path
from .views import home_view,form_view,users_view

urlpatterns = [
    path('', home_view, name='home_view'),
    path('form', form_view, name='form_view'),
    path('users', users_view, name='users_view'),
]

