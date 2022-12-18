from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from gotya.forms import AddContentModelForm
from gotya.models import ContentModel
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ContentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    template_name= 'pages/update-content.html'
    fields = ('header', "text", "picture")

    def get_object(self):
        content = get_object_or_404(
            ContentModel,
            slug= self.kwargs.get('slug'),
            user = self.request.user
            )
        return content

    def get_success_url(self):
        return reverse("detail", kwargs={
            'slug' : self.get_object().slug #First parameter is to send URL, 2nd which parameters comes for that URL
        }) 