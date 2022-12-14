from django.contrib.auth.forms import UserChangeForm
from account.models import CustomUserModel

class ProfileEdit(UserChangeForm):
    password = None
    class Meta:
        model= CustomUserModel
        fields = ('email', 'username','first_name', 'last_name', 'avatar')