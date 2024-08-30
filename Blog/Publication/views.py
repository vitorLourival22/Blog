# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from blog import settings
from .forms import SignUpForm, LoginForm , PublicationForm,
from .models import Publication


def index(request):
    return render(request, 'index.html')

def page(request):
    Publications = Publication.objects.all()
    return render(request, 'index1.html', {'Publications': Publications})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def posted(request):
    return render(request, 'posted.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona para a página de login após o cadastro bem-sucedido
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('page')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def posted(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            Publication = form.save()
            return redirect('page')
    else:
        form = PublicationForm()
    return render(request, 'posted.html', {'form': form})

def delete_publication(request, pk):
    publication = Publication.objects.get(pk=pk)
    if request.method == 'POST':
        publication.delete()
        return redirect('page')
    return render(request, 'delete_publication.html', {'publication': publication})

def publicacao(request):
    return render(request, 'publicação.html')

def edit_publication(request, pk):
    publication = Publication.objects.get(pk=pk)
    if request.method == 'POST':
        form = PublicationForm(request.POST, instance=publication)
        if form.is_valid():
            form.save()
            return redirect('page')
    else:
        form = PublicationForm(instance=publication)
    return render(request, 'edit_publication.html', {'form': form})

def publicacao_detail(request, pk):
    publication = Publication.objects.get(pk=pk)
    return render(request, 'publicacao_detail.html', {'publication': publication})