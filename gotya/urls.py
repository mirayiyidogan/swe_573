import imp
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.http import HttpResponse
from gotya.views import communicate, homepage, category, myspace, detail, create_content, update_content, delete_content, delete_comment
from django.conf.urls.static import static #Static function helps us to publish media files at prod creating url pattern
from django.conf import settings


urlpatterns = [
    path('', homepage, name='homepage'),
    path("communication", communicate, name='communication'),
    path('category/<slug:categorySlug>', category, name='category'),
    path('myspace', myspace, name='myspace'),
    path('detail/<slug:slug>', detail, name='detail'),
    path('create-content', create_content, name='create-content'),
    path('update-content/<slug:slug>', update_content, name='update-content'),
    path('delete-content/<slug:slug>', delete_content, name='delete-content'),
    path('delete-comment/<int:id>', delete_comment, name='delete-comment'),

] 