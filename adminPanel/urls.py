from django.contrib import admin
from django.urls import path, include
from .views import Index


urlpatterns = [
    path('', Index.as_view(), name='index')
]
