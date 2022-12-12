from django.shortcuts import render, redirect, reverse
from gotya.forms import AddContentModelForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from gotya.models import ContentModel

class ContentCreateView(CreateView):
    template_name= 'pages/create-content.html'
    model= ContentModel
    fields= ('header', "text", "picture")

    def get_success_url(self):
        return reverse('detail', kwargs={
            'slug' : self.object.slug
        })

    def form_valid(self, form):
        content = form.save(commit=False)
        content.user = self.request.user
        content.save()
        form.save_m2m()
        return super().form_valid(form)