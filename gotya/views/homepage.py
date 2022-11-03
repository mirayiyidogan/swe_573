
from django.shortcuts import render


def homepage(request):
    context = {
        "name" : "Miray İyidoğan"
    }
    return render(request, 'pages/home.html', context=context) 