from django.contrib.auth.forms import UserCreationForm

from pypro.base.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'email', 'password1', 'password2')
