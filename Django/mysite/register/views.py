from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def signup(response):
    if response.method == 'POST':
      form = UserCreationForm(response.POST)
      if form.is_valid():
        form.save()
    else:
      form =UserCreationForm()
    
    return render(response,'signup.html',{'form':form})

def login(reponse):
    return render(response,'login.html')
