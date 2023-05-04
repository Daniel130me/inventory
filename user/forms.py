from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    # address = forms.CharField(required=True)
    # phone_number = forms.CharField(required=True)
    # image = forms.ImageField(required=True)
    # age = forms.IntegerField(required=True)
    # gender = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone']