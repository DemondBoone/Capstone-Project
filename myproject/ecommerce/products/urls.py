from django.urls import path
from . import views
from apitest import views as apitest_views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', apitest_views.test_ebay_api, name='test_ebay_api'),
]