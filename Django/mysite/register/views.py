from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import RegisterForm


def signup(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        print(form['email'].value())
        print(form['username'].value())
        print(form['password1'].value())
        print(form['password2'].value())
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterForm()

    return render(response, 'signup.html', {'form': form})

# def login(response):
#     return render(response, 'login.html')

