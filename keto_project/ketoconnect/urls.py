from django.contrib import admin
from django.urls import path
from ketoconnect import views
from django.conf import settings

urlpatterns = [
    path('keto-age/',views.ketoAge),
    path('userdetails/',views.UserDetails),
]