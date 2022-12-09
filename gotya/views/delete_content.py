from django.contrib.auth.decorators import login_required
from gotya.models import ContentModel
from django.shortcuts import get_object_or_404,redirect
from django.views.generic import DeleteView
from django.urls import reverse_lazy

#@login_required(login_url='/')
class ContentDeleteView(DeleteView):
    template_name= 'pages/delete_content_confirm.html'
    success_url= reverse_lazy('myspace')

    def get_queryset(self):
        content = ContentModel.objects.filter(slug=self.kwargs['slug'], user=self.request.user)
        return content



