from django.urls import path
from . import views


urlpatterns = [
  path('signupform/',views.signupform, name='formprom'),
  path('dashboard/',views.dashboard, name='dashboard'),
  path('navbar/',views.navbar, name='navbar'),

]
