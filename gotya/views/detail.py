from django.shortcuts import render, get_object_or_404
from gotya.models import ContentModel

def detail(request, slug):
    content = get_object_or_404(ContentModel, slug=slug)
    comments = content.comments.all()
    return render(request, 'pages/detail.html', context={
        'content' : content, 
        'comments': comments,
    })
    