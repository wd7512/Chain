from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(response):
  return render(response, 'home.html',{'title': 'Welcome to'})

def profile_prom(response):
  return render(response, 'profile_prom.html')

def profile_comp(response):
  return render(response, 'profile_comp.html')

def contact(response):
  return render(response, 'contact.html',{'title': 'Contact'})
