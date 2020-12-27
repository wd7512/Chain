from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:  # define the fact this register form is saving into the users database
        model = User
        fields = ["username", "email", "password1", "password2"]
