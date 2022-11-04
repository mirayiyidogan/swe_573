from django.shortcuts import render
from multiprocessing import context

def homepage(request):
    context = {
        "name" : "Miray İyidoğan"
    }
    return render(request, 'pages/home.html', context=context) 