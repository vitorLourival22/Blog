from .views import index , about , contact , login , signup , page, posted
from django.urls import path
from . import views

urlpatterns = [
    path('',index,name='index'),
    path('page/',views.page,name='page'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('login/',login, name='login'),
    path('signup/', signup, name='signup'),   
    path('posted/', views.posted, name='posted'),
    path('delete_publication/<pk>/', views.delete_publication, name='delete_publication'),
    ]
