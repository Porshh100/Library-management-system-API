<<<<<<< HEAD
"""
URL configuration for Library_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
=======

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def root_view(request):
    return HttpResponse("<h2>Welcome to the Library Management System API</h2><p>Visit <a href='/api/'>/api/</a> for API endpoints.</p>")

urlpatterns = [
    path('', root_view),
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),
>>>>>>> 17c612a (Added serializers, views, and URLs for API endpoints)
]
