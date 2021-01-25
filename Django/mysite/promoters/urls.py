from django.urls import path
from . import views


urlpatterns = [
  path('signupform/',views.signupform, name='promoter_init_form'),
  path('dashboard/',views.dashboard, name='promoter_dashboard'),
]
