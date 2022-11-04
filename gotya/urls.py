import imp
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.http import HttpResponse
from gotya.views import communicate, homepage
from django.conf.urls.static import static #Static function helps us to publish media files at prod creating url pattern
from django.conf import settings


urlpatterns = [
    path('', homepage),
    path("communication", communicate),
] 