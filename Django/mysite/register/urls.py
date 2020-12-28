from django.urls import path, include
from . import views

urlpatterns = [
    path('register/',views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.login_view, name='home'),
    #path('login/', views.login, name='contact'),
    #path('', include("django.contrib.auth.urls")), #built in login
    #path('signup/', views.signup, name='signup'),
]


