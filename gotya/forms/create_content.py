from django import forms
from gotya.models import ContentModel

class AddContentModelForm(forms.ModelForm):
    class Meta:
        model = ContentModel
        exclude = ("user", "slug")
        