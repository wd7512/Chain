from django.urls import path
from . import views

urlpatterns = [
  path('signup/',views.signup, name='home'),
  path('login/',views.login, name='contact')
]
