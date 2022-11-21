from django import forms

class CommunicationForm(forms.Form):
    email = forms.EmailField(max_length=100)
    name_surname = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)
