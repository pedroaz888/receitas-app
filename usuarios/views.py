from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if not nome.strip():
            print('nome não pode ser nulo')
            return redirect('cadastro')
        if not email.strip():
            print('email não pode ser nulo')
            return redirect('cadastro')
        if password != password2:
            print('senhas não correspondem')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('Usuário já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=password)
        user.save()
        print('Usuário cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['senha']
        if email == "" or password == "":
            print("os campos não podem ser nulos")
            return redirect('login')
        print(email, password)
        return redirect ('dashboard')
    return render(request, 'usuarios/login.html')

def logout(request):
    pass

def dashboard(request):
    return render(request, 'usuarios/dashboard.html')
