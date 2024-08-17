from . views import index , about , contact , login , signup
from django.urls import path

urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('login/',login, name='login'),
    path('signup/', signup, name='signup'),    
]
