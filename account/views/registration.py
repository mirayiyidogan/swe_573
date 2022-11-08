from django.shortcuts import render,redirect
from account.forms import registrationform
from django.contrib.auth import login as django_login, authenticate
#from django.contrib import messages


def registration(request):
    if request.method== 'POST':
         form = registrationform(request.POST)
         if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            django_login(request, user)
            return redirect('homepage')
            #message.success(request, 'Your profile has been updated.')
    else:
        form = registrationform()
    return render(request, 'pages/registration.html', context={
        'form' : form
    })
