from django.shortcuts import render
from .forms import init_form

# Create your views here.
def signupform(request):
  form = init_form(request.POST or None)
  return render(request, "promoters/plain_form.html", {"form": form})
