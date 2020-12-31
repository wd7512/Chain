from django.shortcuts import render, redirect
from .forms import init_form
from .models import company_form
from django.contrib import messages
from django.utils import timezone

# Create your views here.
def signupform(request):
  form = init_form(request.POST or None)
  if form.is_valid():
    username = form.cleaned_data.get("username")
    company_name = form.cleaned_data.get("company_name")
    submission_date = timezone.now()

    dataline = company_form(username=username,
                company_name = company_name,
                submission_date = submission_date,
                )
    dataline.save()
    return redirect('/companies/dashboard/')
    
    
    
  return render(request, "plain_form.html", {"form": form})

def dashboard(request):
  return render(request,"companies/dashboard.html")
