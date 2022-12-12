import imp
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.http import HttpResponse
from gotya.views import communicate, homepage, category, myspace, DetailView, ContentCreateView, ContentUpdateView, ContentDeleteView, delete_comment
from django.conf.urls.static import static #Static function helps us to publish media files at prod creating url pattern
from django.conf import settings
from django.views.generic import TemplateView,RedirectView


urlpatterns = [
    path('', homepage, name='homepage'),
    path("communication", communicate, name='communication'),
    path('about', TemplateView.as_view(
        template_name ='pages/about.html'
    ), name='about'),
    path("redirect", RedirectView.as_view(
        url='http://www.google.com'
    ), name='redirect'),
    path('category/<slug:categorySlug>', category, name='category'),
    path('myspace', myspace, name='myspace'),
    path('detail/<slug:slug>', DetailView.as_view(), name='detail'),
    path('create-content', ContentCreateView.as_view(), name='create-content'),
    path('update-content/<slug:slug>', ContentUpdateView.as_view(), name='update-content'),
    path('delete-content/<slug:slug>', ContentDeleteView.as_view(), name='delete-content'),
    path('delete-comment/<int:id>', delete_comment, name='delete-comment'),

] 