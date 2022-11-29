from django.contrib.auth.decorators import login_required
from gotya.models import ContactModel
from django.shortcuts import get_object_or_404,redirect

@login_required(login_url='/')
def delete_content(request, slug):
    get_object_or_404(ContactModel, slug=slug, user=request.user).delete()
    return redirect('myspace')
