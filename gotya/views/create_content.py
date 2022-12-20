from django.shortcuts import reverse
from django.urls import reverse_lazy, reverse
from gotya.forms import AddContentModelForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from gotya.models import ContentModel
from django.contrib.auth.mixins import LoginRequiredMixin

class ContentCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    template_name= 'pages/create-content.html'
    model= ContentModel
    fields= ('header', "text", "picture", "url")

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