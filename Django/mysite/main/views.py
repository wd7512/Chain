from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(response):
  return render(response, 'home.html',{'title': 'Welcome to'})

def contact(response):
  return render(response, 'contact.html',{'title': 'Contact'})
