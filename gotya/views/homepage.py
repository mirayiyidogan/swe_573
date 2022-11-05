from django.shortcuts import render
from multiprocessing import context
from gotya.models import ContentModel
from django.core.paginator import Paginator

def homepage(request):
    contents = ContentModel.objects.order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(contents, 2)

    return render(request, 'pages/home.html', context={
        'contents' : paginator.get_page(page)
    }) 

    