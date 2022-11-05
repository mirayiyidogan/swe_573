from multiprocessing import context
from django.shortcuts import render

def communicate(request):
    context = {
        'key': 'header content whatsapp '
    }
    return render(request, 'pages/communication.html', context=context) #render function will look up template files for context