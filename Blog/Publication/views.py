# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import SignUpForm, LoginForm , PostForm

def index(request):
    return render(request, 'index.html')

def page(request):
    return render(request, 'index1.html')

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

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Atribua o usuário atual à postagem
            post.save()
            return redirect('post_success')  # Redirecionar para uma página de sucesso ou lista de postagens
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})