"""mynewsproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from mynewsapp import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('world',views.world,name='world'),
    path('sports',views.sports,name='sports'),
    path('entertainment',views.entertainment,name='entertainment'),
    path('business',views.business,name='business'),
    path('finance',views.finance,name='finance'),
    path('tech',views.tech,name='tech'),
    path('trending',views.trending,name='trending'),

]

urlpatterns += staticfiles_urlpatterns()
