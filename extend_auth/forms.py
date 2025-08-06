from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile

class signup_form(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(signup_form, self).__init__(*args, **kwargs)
        ru_label = {
            'username': 'Логин',
            'email': 'email',
            'password1': 'пароль',
            'password2': 'Подтверждение пароля'
        }
        self.error_messages.update({
            'password_mismatch':'Пароли не совпадают'
        })
        self.fields['username'].error_messages['unique'] = f'Логин занят'
        self.fields['email'].error_messages['invalid'] = f'Неверный формат почтового адреса'
        for k, field in self.fields.items():
            field.error_messages['required'] = f'Поле "{ru_label[k]}" обязательно!'


    def clean_email(self):
        cleaned_email = self.cleaned_data.get('email')
        if cleaned_email == '':
            raise ValidationError("Неверный формат почтового адреса", code='invalid')
        elif User.objects.filter(email=cleaned_email).exists():
            raise ValidationError("Почта уже привязана к другому аккаунту", code='unique')
        return cleaned_email

class email_change_form(forms.Form):
    error_messages = {
        'password_error': "Неправильный пароль",
        'email_mismatch': "Введённые адреса электронной почты не совпадают",
        'not_changed': "Адрес электронной почты совпадает с уже привязанным к пользователю",
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

class avatar_change_form(forms.Form):
    avatar = forms.ImageField()

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(avatar_change_form, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            Profile.objects.update_or_create (
                user=self.user,
                defaults={"portrait": self.cleaned_data["avatar"]}
            )