from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile

class signup_form(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']

    def clean_email(self):
        cleaned_email = self.cleaned_data.get('email')
        if User.objects.filter(email=cleaned_email).exists():
            raise ValidationError("Почта уже привязана к другому аккаунту")
        return cleaned_email

class email_change_form(forms.Form):
    error_messages = {
        'password_error': "Неправильный пароль",
        'email_mismatch': "The two email addresses fields didn't match.",
        'not_changed': "The email address is the same as the one already defined.",
    }

    password1 = forms.CharField(
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "password"})
    )

    new_email1 = forms.EmailField(
        label= "New email address",
        required=True,
        widget=forms.EmailInput,
    )

    new_email2 = forms.EmailField(
        label= "New email address confirmation",
        required=True,
        widget=forms.EmailInput,
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(email_change_form, self).__init__(*args, **kwargs)

    def clean_password1(self):
        user_password = self.cleaned_data.get('password1')
        if not self.user.check_password(user_password):
            raise forms.ValidationError(
                self.error_messages['password_error'],
                code='password_error',
            )
        return user_password

    def clean_new_email1(self):
        old_email = self.user.email
        new_email1 = self.cleaned_data.get('new_email1')
        if new_email1 and old_email:
            if new_email1 == old_email:
                raise forms.ValidationError(
                    self.error_messages['not_changed'],
                    code='not_changed',
                )
        return new_email1

    def clean_new_email2(self):
        new_email1 = self.cleaned_data.get('new_email1')
        new_email2 = self.cleaned_data.get('new_email2')
        if new_email1 and new_email2:
            if new_email1 != new_email2:
                raise forms.ValidationError(
                    self.error_messages['email_mismatch'],
                    code='email_mismatch',
                )
        return new_email2

    def save(self, commit=True):
        email = self.cleaned_data["new_email1"]
        self.user.email = email
        if commit:
            self.user.save()
        return self.user