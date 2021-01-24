from django.shortcuts import render, redirect
from .forms import init_form
from .models import user_form
from django.contrib import messages
from django.utils import timezone

# Create your views here.
def signupform(request):
  if request.user.init_form_complete == 1 : #if form is complete, never go back, otherwise we keep making copies for the same user
      return redirect('/promoters/dashboard/')

  form = init_form(request.POST or None)
  if form.is_valid():
    username = form.cleaned_data.get("username")
    insta_id = form.cleaned_data.get("ig_name")
    sex = form.cleaned_data.get("sex")
    birthday = form.cleaned_data.get("birthday")
    submission_date = timezone.now()
    followers = form.cleaned_data.get("followers")
    dataline = user_form(username=username,
                instagram_id = insta_id,
                submission_date = submission_date,
                sex = sex,
                birthday = birthday,
                followers = followers)
    request.user.init_form_complete = 1
    request.user.save()
    dataline.save()
    return redirect('/promoters/dashboard/')
  return render(request, "plain_form.html", {"form": form})

def dashboard(request):
    if request.user.init_form_complete == 1 : #form complete
        return render(request,"dashboard.html")
    return redirect('promoters/signupform')

def navbar(request):
  return render(request,"navbar.html")

