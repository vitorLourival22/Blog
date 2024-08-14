from . views import contato , login
from django.urls import path

urlpatterns = [
    path('',contato,name='contato'),
]