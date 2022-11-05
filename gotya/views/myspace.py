from django.shortcuts import render, get_object_or_404
from multiprocessing import context
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def myspace(request):
    contents= request.user.contents.order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(contents, 3)

    return render(request, 'pages/myspace.html', context={
        'contents' : paginator.get_page(page),
    }) 

    