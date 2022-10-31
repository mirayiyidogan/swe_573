from django.shortcuts import render
from django.http import HttpResponse

def communicate(request):
    return HttpResponse("<h1> Hi! <h1>")