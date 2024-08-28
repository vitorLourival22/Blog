from .views import index , about , contact , login , signup , page, posted, publicacao
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name='index'),
    path('page/',views.page,name='page'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('login/',login, name='login'),
    path('signup/', signup, name='signup'),   
    path('posted/', views.posted, name='posted'),
    path('delete_publication/<pk>/', views.delete_publication, name='delete_publication'),
    path('publicacao/<pk>/editar/', views.edit_publication, name='edit_publication'),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

