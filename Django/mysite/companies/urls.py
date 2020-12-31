from django.urls import path
from . import views

urlpatterns = [
  #path('',views.home, name='home'),
  path('signupform/',views.signupform, name='form'),
  path('dashboard/',views.dashboard, name = 'dashboard'),
]
