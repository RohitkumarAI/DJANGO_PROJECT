from django.contrib import admin
from django.urls import path
from app.views import movie

urlpatterns = [
    path('/',name='movie'),
]
