from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

# URLS just remember how it goes, path, view, name 
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'), 
    path('login/', LoginView.as_view(template_name='profiles/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
]