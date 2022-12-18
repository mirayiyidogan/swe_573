from multiprocessing import context
from django.shortcuts import render, redirect
from gotya.forms import CommunicationForm
from gotya.models import ContactModel
from django.views.generic import FormView

class CommunicationFormView(FormView):
    template_name= 'pages/communication.html'
    form_class= CommunicationForm
    success_url='/mail-sent'


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)