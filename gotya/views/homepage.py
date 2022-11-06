from django.shortcuts import render
from multiprocessing import context
from gotya.models import ContentModel
from django.core.paginator import Paginator
from django.db.models import Q

def homepage(request):
    search = request.GET.get('search')
    contents = ContentModel.objects.order_by('-id')
    if search:
        contents = contents.filter(
            Q(header__icontains=search) | Q(text__icontains=search)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(contents, 2)

    return render(request, 'pages/home.html', context={
        'contents' : paginator.get_page(page)
    }) 

    