# bruno/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView



urlpatterns = [
    path('', include('contact_manager.urls')),
]
