from django.shortcuts import render, redirect
from .forms import init_form
from .models import company_form
from django.contrib import messages
from django.utils import timezone


# Create your views here.
def signupform(request):
    # if request.user.init_form_complete == 1 : #if form is complete, never go back, otherwise we keep making copies for the same user
    #     return redirect('/companies/dashboard/')
    form = init_form(request.POST or None)
    if form.is_valid():
        email = request.user.email
        company_name = form.cleaned_data.get("company_name")
        company_size = form.cleaned_data.get("company_size")
        company_business_area = form.cleaned_data.get("company_business_area")
        company_instagram_id = form.cleaned_data.get("company_instagram_id")
        submission_date = timezone.now()
        dataline = company_form(email=email,
                                company_name=company_name,
                                company_size=company_size,
                                company_business_area=company_business_area,
                                company_instagram_id=company_instagram_id,
                                submission_date=submission_date,
                                )
        request.user.init_form_complete = 1
        request.user.save()
        dataline.save()

        return redirect('/companies/dashboard/')

    return render(request, "plain_form.html", {"form": form})


def dashboard(request):
    return render(request, "dashboardcompany.html",{'email': request.user.email})
