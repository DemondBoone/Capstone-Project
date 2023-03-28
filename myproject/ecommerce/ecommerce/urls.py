"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from profiles.views import profile
from apitest import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('', include('profiles.urls')),  # Remove 'profile/'
    path('accounts/', include('django.contrib.auth.urls')),
    path('products/', include('apitest.urls')),
    path('', include('apitest.urls')),
    path('accounts/profile/', profile, name='profile'),
    path('products/', views.test_ebay_api, name='test_ebay_api'),  
]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('products.urls')),
#     path('', include('profiles.urls')),  # Remove 'profile/'
#     path('accounts/', include('django.contrib.auth.urls')),
#     path('products/', include('apitest.urls')),
#     path('', include('apitest.urls')),
#     path('accounts/profile/', profile, name='profile'),
#     path('products/', views.test_ebay_api, name='test_ebay_api'),  # Update the path here
# ]