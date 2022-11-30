from django import forms
from gotya.models import CommentModel

class AddCommentFormModel(forms.ModelForm):
    class Meta:
        model= CommentModel
        fields = ('comment',)