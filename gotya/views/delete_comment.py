from django.contrib.auth.decorators import login_required
from gotya.models import CommentModel
from django.shortcuts import get_object_or_404,redirect
from django.contrib import messages

@login_required(login_url='/')
def delete_comment(request, id):
    comment= get_object_or_404(CommentModel, id= id)
    if comment.user == request.user or comment.content.user == request.user:
        comment.delete()
        messages.success(request, 'Comment has been deleted successfully.')
        return redirect('detail', slug=comment.content.slug)
    return redirect('homepage')
