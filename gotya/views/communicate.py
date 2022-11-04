from multiprocessing import context
from django.shortcuts import render

def communicate(request):
    return render(request, 'pages/communication.html', context={}) #render function will look up template files for context