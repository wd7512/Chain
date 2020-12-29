from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm

User = get_user_model()


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        type_client = form.cleaned_data.get("type_client")
        password = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")
        try:
            user = User.objects.create_user(username, email, password)
        except:
            user = None
        if user != None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request,"Invalid email or password")
            request.session['register_error'] = 1
    return render(request, "register/forms.html", {"form": form})


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user != None:
            # user is valid and active -> is_active
            # request.user == user
            login(request, user)
            return redirect("user_dashboard/")
        else:
            # attempt = request.session.get("attempt") or 0
            # request.session['attempt'] = attempt + 1
            # return redirect("/invalid-password")
            messages.error(request, "invalid email of password")
            request.session['invalid_user'] = 1  # 1 == True
    return render(request, "register/forms.html", {"form": form})


def logout_view(request):
    logout(request)
    # request.user == Anon User
    return redirect("/login")

def user_dashboard(request):
    return render(request, "dashboards/user_dashboard.html")

def company_dashboard(request):
    return render(request, "dashboards/company_dashboard.html")
