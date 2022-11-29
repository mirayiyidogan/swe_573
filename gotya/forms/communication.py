from django import forms
from gotya.models import ContactModel

class CommunicationForm(forms.ModelForm):
    class Meta:
        model= ContactModel
        fields = ('name_surname', 'email', 'message')