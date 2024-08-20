from . views import index , about , contact , login , signup , page, posted
from django.urls import path

urlpatterns = [
    path('',index,name='index'),
    path('page/',page,name='page'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('login/',login, name='login'),
    path('signup/', signup, name='signup'),   
    path('posted/', posted, name='posted'),
]
