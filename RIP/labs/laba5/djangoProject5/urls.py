"""djangoProject5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.GetFilms),
    path('comedy/', views.GetComedy),
    path('melodrama/', views.GetMelodrama),
    path('scifi/', views.GetSciFi),
    path('film1/', views.GetFilm1),
    path('film2/', views.GetFilm2),
    path('film3/', views.GetFilm3),
    path('film4/', views.GetFilm4),
    path('film5/', views.GetFilm5),
    path('film6/', views.GetFilm6)
]
