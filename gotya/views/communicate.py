from multiprocessing import context
from django.shortcuts import render, redirect
from gotya.forms import CommunicationForm
from gotya.models import ContactModel

def communicate(request):
    form = CommunicationForm()
    if request.method == 'POST':
        form = CommunicationForm(request.POST)
        if form.is_valid():
            contact = ContactModel()
            contact.email = form.cleaned_data['email']
            contact.name_surname = form.cleaned_data['name_surname']
            contact.message = form.cleaned_data['message']
            contact.save()
            return redirect('homepage')
        #else:
    context = {
        'form': form
    }
    return render(request, 'pages/communication.html', context=context) #render function will look up template files for context