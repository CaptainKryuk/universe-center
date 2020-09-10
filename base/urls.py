from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from universe import settings

from .views import index

urlpatterns = [
    path('', index, name="index"),
]
