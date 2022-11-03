from multiprocessing import context
from django.shortcuts import render

def communicate(request):
    context = {
        "name" : "Miray İyidoğan"
    }
    return render(request, 'pages/home.html', context=context) #render function will look up template files for context