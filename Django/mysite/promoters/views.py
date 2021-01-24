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
    username = request.user.email
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
    email = request.user.email
    query = user_form.objects.all
    passemail = user_form.objects.get(username = email)
    row = user_form.objects.all().filter(username = email).values_list()
    id = row[0][0] # id
    #emaill = row[0][1] # email
    instagram_id = row[0][2] # instagram_id
    sex = row[0][3] # sex
    submission_date = row[0][4] # submission_date
    birthday = row[0][5] # birthday
    followers = row[0][6] # followers
    return render(request, "dashboard.html", {'email': passemail,
                                              'all':list(row),
                                              'instagram_id': instagram_id,
                                              'sex': sex,
                                              'submission_date':submission_date,
                                              'birthday':birthday,
                                              'followers':followers})

def navbar(request):
  return render(request,"navbar.html")

