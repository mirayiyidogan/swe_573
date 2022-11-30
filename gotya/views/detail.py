from django.shortcuts import render, get_object_or_404
from gotya.models import ContentModel
from gotya.forms import AddCommentFormModel

def detail(request, slug):
    content = get_object_or_404(ContentModel, slug=slug)
    comments = content.comments.all()

    if request.method == 'POST':
        add_comment_form = AddCommentFormModel(request.POST)
        if add_comment_form.is_valid():
            comment = add_comment_form.save(commit=False)
            comment.user = request.user
            comment.content = content
            comment.save()
    add_comment_form = AddCommentFormModel()
    return render(request, 'pages/detail.html', context={
        'content' : content, 
        'comments': comments,
        'add_comment_form': add_comment_form,
    })
    