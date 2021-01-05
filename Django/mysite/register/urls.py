from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.registration_view, name='register'),
    path('login/', views.login_view, name='login')
]



'''
urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.login_view, name='home'),
    path("user_dashboard/", views.user_dashboard, name='user_dashboard'),
    path("company_dashboard/", views.company_dashboard, name='user_dashboard')
    # path('login/', views.login, name='contact'),
    # path('', include("django.contrib.auth.urls")), #built in login
    # path('signup/', views.signup, name='signup'),
]

'''
