from django.shortcuts import render, get_object_or_404, redirect
from gotya.models import ContentModel
from gotya.forms import AddCommentFormModel
from django.views import View
from django.contrib import messages

class DetailView(View):
    http_method_names = ['get', 'post']
    add_comment_form = AddCommentFormModel

    def get(self, request, slug):
        content = get_object_or_404(ContentModel, slug=slug)
        comments = content.comments.all()
        return render(request, 'pages/detail.html', context={
            'content' : content, 
            'comments': comments,
            'add_comment_form': self.add_comment_form()
        })
    
    def post(self, request, slug):
        content = get_object_or_404(ContentModel, slug=slug)
        add_comment_form = self.add_comment_form(data=request.POST)
        if add_comment_form.is_valid():
            comment = add_comment_form.save(commit=False)
            comment.user = request.user
            comment.content = content
            comment.save()
            messages.success(request, "Comment added successfully.")
        return redirect('detail', slug=slug)


    