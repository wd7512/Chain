from django.urls import path
from . import views

urlpatterns = [
  path('signupform/',views.signupform, name='form'),
  path('dashboard/',views.dashboard, name='dashboard'),
  path('testpage/',views.test, name='testpage'),
  path('navbar/',views.navbar, name='navbar')
]
