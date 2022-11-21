from django import forms

class CommunicationForm(forms.Form):
    email = forms.EmailField(max_length=100)
    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea)
