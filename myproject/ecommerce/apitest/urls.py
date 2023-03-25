from django.urls import path
from . import views

urlpatterns = [
    path('apitest/test-api/', views.test_ebay_api, name='test_ebay_api'), #this will call for the testebay api remember there is three parts in this
    path('laptops/', views.test_ebay_api, name='laptops'), #path view name
]