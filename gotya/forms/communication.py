from django import forms
from gotya.models import ContactModel
from django.core.mail import send_mail

class CommunicationForm(forms.ModelForm):
    class Meta:
        model= ContactModel
        fields = ('name_surname', 'email', 'message')

    def send_email(self, message):
        send_mail(
            subject = "Notification from Gotya",
            message= message,
            from_email=None,
            recipient_list=['miray.iyidogan.m@gmail.com'],
            fail_silently=False
        )
