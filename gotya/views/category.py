from django.shortcuts import render, get_object_or_404
from multiprocessing import context
from gotya.models import ContentModel, CategoryModel
from django.core.paginator import Paginator

def category(request, categorySlug):
    category = get_object_or_404(CategoryModel, slug=categorySlug)
    #contents = ContentModel.objects.order_by('-id')
    contents= category.content.order_by('-id')
    print(contents)
    page = request.GET.get('page')
    paginator = Paginator(contents, 2)

    return render(request, 'pages/category.html', context={
        'contents' : paginator.get_page(page),
        'category_name' : category.name
    }) 

    