from django.urls import path,include
from . import views




urlpatterns = [
  path('',views.home, name='home'),
  path('profile_prom/',views.profile_prom, name='profile_prom'),
  path('profile_comp/',views.profile_comp, name='profile_comp'),
  path('contact/',views.contact, name='contact'),
  path('promoters/', include('promoters.urls')),
]
