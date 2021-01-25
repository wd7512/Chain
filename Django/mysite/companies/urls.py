from django.urls import path
from . import views


urlpatterns = [
  #path('',views.home, name='home'),
  path('signupform/',views.signupform, name='company_init_form'),
  path('dashboard/',views.dashboard, name='company_dashboard'),
]


