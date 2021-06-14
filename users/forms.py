from django.forms import ModelForm
from users.models import Profile


class UserForm(ModelForm):
    class Meta:
        Model = Profile
        fields = ['user', 'nickname', 'image', 'bio']