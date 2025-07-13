from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class signup_form(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']

    def clean_email(self):
        cleaned_email = self.cleaned_data.get('email')
        if User.objects.filter(email=cleaned_email).exists():
            raise ValidationError("Почта уже привязана к другому аккаунту")
        return cleaned_email