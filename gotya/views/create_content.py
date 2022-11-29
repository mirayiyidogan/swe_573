from django.shortcuts import render, redirect
from gotya.forms import AddContentModelForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def create_content(request):
    form = AddContentModelForm(request.POST or None, files = request.FILES or None)
    if form.is_valid():
        content = form.save(commit=False)
        content.user = request.user
        content.save()
        form.save_m2m()
        return redirect('detail', slug=content.slug)
    return render(request, "pages/create-content.html", context={
        'form': form
    })