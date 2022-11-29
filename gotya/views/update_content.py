from django.shortcuts import render, redirect, get_object_or_404
from gotya.forms import AddContentModelForm
from gotya.models import ContentModel
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def update_content(request, slug):
    content = get_object_or_404(ContentModel, slug=slug, user=request.user)
    form = AddContentModelForm(request.POST or None, files=request.FILES or None, instance=content)
    if form.is_valid():
        form.save()
        return redirect("detail", slug=content.slug)
    return render(request, "pages/update-content.html", context={
        'form': form
    })