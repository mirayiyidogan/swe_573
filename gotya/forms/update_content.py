from django import forms
from gotya.models import ContentModel

class UpdateContentFormModel(forms.ModelForm):
    class Meta:
        model = ContentModel
        exclude = ("user", "slug")
        