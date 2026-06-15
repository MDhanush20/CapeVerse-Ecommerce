from django import forms
from django.contrib.auth.hashers import make_password
from .models import capesign


class capesignup(forms.ModelForm):
    class Meta:
        model = capesign
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(user.password)

        if commit:
            user.save()

        return user