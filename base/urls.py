from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from universe import settings

from .views import index, gallery

urlpatterns = [
    path('', index, name="index"),
    path('gallery', gallery, name="gallery")
]
