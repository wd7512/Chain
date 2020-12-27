from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    #path('login/', views.login, name='contact'),
    path('', include("django.contrib.auth.urls")), #built in login
]
