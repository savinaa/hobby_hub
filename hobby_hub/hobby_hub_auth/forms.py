from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class SignInForm(forms.Form):
    user=None
    email=forms.EmailField(

    )
    password = forms.CharField(
        max_length=15,
        widget=forms.PasswordInput(),
    )

    def clean_password(self):
        self.user=authenticate(
                email=self.cleaned_data['email'],
                password=self.cleaned_data['password'],
            )

        if not self.user:
            raise ValidationError('Email and/or password not correct!')

    def save(self):
        return self.user