from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from account.forms import ProfileEdit
#from django.contrib.auth.forms import PasswordChangeForm
#from django.contrib import messages

@login_required(login_url='/')
def profile_update(request):
    if request.method== 'POST':
        form = ProfileEdit(request.POST, request.FILES, instance= request.user)
        if form.is_valid():
            form.save()
            #message.success(request, 'Your profile has been updated.')
    else:
        form = ProfileEdit()
    return render(request, 'pages/profile-update.html', context={
        'form' : form
    })
