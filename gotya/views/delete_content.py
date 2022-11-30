from django.contrib.auth.decorators import login_required
from gotya.models import ContentModel
from django.shortcuts import get_object_or_404,redirect

@login_required(login_url='/')
def delete_content(request, slug):
    get_object_or_404(ContentModel, slug= slug, user= request.user).delete()
    return redirect('myspace')
