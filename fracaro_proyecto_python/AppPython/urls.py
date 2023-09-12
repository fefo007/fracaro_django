
from django.urls import path
from AppPython.views import *

urlpatterns = [
    path('',login,name='login'),    
    path('home/',home,name='home'),
    path('travels/',travels,name='travels'),
    path('contact/',contact,name='contact'),
    path('about-us/',aboutUs,name='about'),
    path('orders/',orders,name='orders'),
    path('user/',user,name='user'),
    path('search/',search,name='search')
]
