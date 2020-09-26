from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from universe import settings

from .views import index, gallery, sport_section, contact_form, requisites_view

urlpatterns = [
    path('', index, name="index"),
    path('sport/<slug:slug>', sport_section),
    path('contact_form', contact_form),
    path('gallery', gallery, name="gallery"),
    path('requisites', requisites_view, name="requisites")
]
