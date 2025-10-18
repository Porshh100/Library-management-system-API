"""
URL configuration for Library_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def root_view(request):
    return HttpResponse("<h2>Welcome to the Library Management System API</h2><p>Visit <a href='/api/'>/api/</a> for API endpoints.</p>")

urlpatterns = [
    path('', root_view),
    path('admin/', admin.site.urls),
    path('api/', include('books.urls'))
]
