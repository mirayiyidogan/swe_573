from django import forms

class CommunicationForm(forms.Form):
    email = forms.EmailField(label='e-mail',max_length=100)
    name_surname = forms.CharField(label='name', max_length=150)
    message = forms.CharField(label="message", widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))
