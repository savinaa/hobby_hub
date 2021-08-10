from django import forms


class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=30,
    )
    password = forms.CharField(
        max_length=15,
        widget=forms.PasswordInput(),
    )