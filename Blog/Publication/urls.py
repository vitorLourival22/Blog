from . views import index , about , contact , login
from django.urls import path

urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('login/',login,name='login'),
    
]
