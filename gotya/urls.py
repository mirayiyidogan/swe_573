import imp
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.http import HttpResponse
from gotya.views import communicate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gotya.urls')),
] 